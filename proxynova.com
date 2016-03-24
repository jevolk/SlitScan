#!/usr/bin/env python2
from harvester import WebParser

url          = "http://www.proxynova.com/proxy-server-list/"
ip_regex     = r'\<span class\=\"row_proxy_ip\"\>\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*\</span\>'
port_regex   = r'(?:left\"\>\s+|\d{2,5}\"\>)(\d{2,5})(?:\s+\</td\>|\</a\>)'

wp = WebParser(url,(ip_regex,port_regex))

for remote in wp.remotes():
	wp.scan(remote)





