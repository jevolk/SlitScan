#!/usr/bin/python

from Harvester import WebParser

url       = "http://www.us-proxy.org/"
regex     = r"\<td\>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\</td\>\<td\>(\d{2,5})"

wp = WebParser(url,regex)
for remote in wp.remotes():
	wp.scan(remote)
