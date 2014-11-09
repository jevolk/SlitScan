#!/usr/bin/python

from Harvester import WebParser

url       = "http://checkerproxy.net/all_proxy"
regex     = r'\<td class\=\"proxy-ipport\"\>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{2,5})\</td\>'

wp = WebParser(url,regex)
for remote in wp.remotes():
	wp.scan(remote)
