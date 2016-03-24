#!/usr/bin/python

import sys
from collections import namedtuple
from harvest.Harvester import Harvester


if len(sys.argv) < 2:
	print "usage: %s <logfile>" % sys.argv[0]
	exit(-1)


harvester = Harvester()
column = namedtuple("Fields","time, symbol, fd, mask, http_code, state_code, state, remote")

for row in open(sys.argv[1]):
	colv, reason = row.split(" : ")
	elem = column._make(colv.split(" "))

	if elem.symbol == "()":
	    print "%d %s" % (float(elem.time),elem.remote)
	    harvester.scan(elem.remote)


