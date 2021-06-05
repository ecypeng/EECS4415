#!/usr/bin/python

import sys
import re

firstLine = True
for inputLine in sys.stdin:
    if not firstLine:
        line = inputLine.split(',')
        businessId = line[0]
        allBusinesses = line[-1]
        businesses = allBusinesses.split(";")
        for i in range(len(businesses)):
            print(str.rstrip(businesses[i]) + '\t' + str(businessId))
    else:
        firstLine = False