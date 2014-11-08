#!/usr/bin/python

from Harvester import WebParser

url         = "http://www.xroxy.com/proxylist.php?port=&type=All_http&pnum=%d"
ip_regex    = r"View this Proxy details.*\>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
port_regex  = r"Select proxies with port number (\d{2,5})"
pages       = 250

wp = WebParser(url,(ip_regex,port_regex),pages)

for remote in wp.remotes():
	wp.scan(remote)

