#!/usr/bin/python

from Harvester import WebParser

url = "http://free-proxy.cz/en/proxylist/main/%d"
# </div> 117.175.231.117</td>
#    <td><span class="fport">8123</span></td>
ip_regex = r"\<\/div\> (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\<\/td\>"
port_regex   = r'\<span\ class\=\"fport\"\>(\d{2,5})\<\/span\>'
pages        = 179

wp = WebParser(url,(ip_regex,port_regex),pages)

for remote in wp.remotes():
        wp.scan(remote)

