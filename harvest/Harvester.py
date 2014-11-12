#!/usr/bin/python
"""
 *  COPYRIGHT 2014 (C) Jason Volk
 *  COPYRIGHT 2014 (C) Svetlana Tkachenko
 *
 *  DISTRIBUTED UNDER THE GNU GENERAL PUBLIC LICENSE (GPL) (see: LICENSE)
"""

import re
import os
import sys
from os import O_NONBLOCK, O_APPEND, O_WRONLY
import urllib2


FIFO_NAME = "harvest.fifo"


class Harvester(object):
	def __init__(self,
	             fifo_name  = FIFO_NAME):
		try:
			self.fifo_path = os.path.dirname(__file__) + "/" + fifo_name
			self.fifo_fd = os.open(self.fifo_path, O_WRONLY | O_APPEND | O_NONBLOCK)
			self.fifo = os.fdopen(self.fifo_fd,'a')
		except OSError as e:
			sys.stderr.write(str(e) + "\n")
			self.fifo = None


	def scan(self,remote):
		sys.stdout.write("%s:%s\n" % (remote[0],remote[1]))
		if self.fifo is not None:
			self.fifo.write("%s:%s\n" % (remote[0],remote[1]))
			self.fifo.flush()



class WebParser(Harvester):
	def __init__(self,
	             url         = None,
	             regex       = None,
	             num_pages   = None,
	             headers     = [('User-agent','Mozilla/5.0')],
	             fifo_name   = FIFO_NAME):
		super(WebParser,self).__init__(fifo_name)
		self.url = url
		self.regex = regex
		self.num_pages = num_pages
		self.headers = headers
		self.opener = urllib2.build_opener()
		self.opener.addheaders = self.headers


	def remotes(self):
		for page in self.pages():
			for remote in self._page_parse(page):
				yield remote


	def pages(self):
		for i in self._page_range(self.num_pages):
			if i is not None:
				yield self._page_fetch((i))
			else:
				yield self._page_fetch()


	def _page_fetch(self,
	                fmtargs  = (),
	                headers  = []):
		self.req_url = self.url % fmtargs
		self.req_req = urllib2.Request(self.req_url)
		for key, val in headers:
			self.req_req.add_header(key, val)

		self.req_resp = self.opener.open(self.req_req)
		self.data = self.req_resp.read()
		return self.data


	def _page_parse(self,
	                data   = None,
	                regex  = None):
		if not data:
			data = self.data

		if not regex:
			regex = self.regex

		if not isinstance(regex, tuple):
			return re.findall(regex,data)

		if len(regex) >= 2 and regex[1] is not None:
			ips = re.findall(regex[0],data)
			ports = re.findall(regex[1],data)
			return zip(ips,ports)

		return re.findall(regex[0],data)


	def _page_range(self, arg):
		if not arg:
			return [None]

		elif isinstance(arg,int):
			return range(arg)

		elif isinstance(arg,tuple) and not any(map(lambda x: x is None, arg)):
			return range(*arg)

		elif isinstance(arg,tuple) and arg[0] is None:
			start = 1 if len(arg) <= 2 else arg[1]
			stop = arg[1] if len(arg) <= 2 else arg[2]
			ret = [""]
			ret.extend(range(start,stop))
			return ret
