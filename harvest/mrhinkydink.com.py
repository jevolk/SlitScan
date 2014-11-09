#!/usr/bin/python

from Harvester import WebParser

url       = "http://www.mrhinkydink.com/proxies%s.htm"
regex     = r'\<td\>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\</td\>\n*\<td\>(\d{2,5})\</td\>'
pages     = (None,2,5)

wp = WebParser(url,regex,pages)
for remote in wp.remotes():
	wp.scan(remote)
