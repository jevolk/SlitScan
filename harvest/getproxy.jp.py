#!/usr/bin/python

from Harvester import WebParser

url          = "http://www.getproxy.jp/default/%d"
ip_regex     = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:\d{2,5}"
port_regex   = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:(\d{2,5})"
pages        = 5

wp = WebParser(url,(ip_regex,port_regex),pages)

for remote in wp.remotes():
	wp.scan(remote)
