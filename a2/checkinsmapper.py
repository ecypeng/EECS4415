#!/usr/bin/python

import sys
import re

outputFile = open('checkinbyday.txt', 'w')
firstLine = True
for inputLine in sys.stdin:
    line = inputLine.split(',')
    businessId = line[0]
    weekDay = line[1]
    numCheckIns = line[3]
    if firstLine:
        firstLine = False
    else:
        outputFile.write(businessId + ", " + weekDay + ", " + numCheckIns)
