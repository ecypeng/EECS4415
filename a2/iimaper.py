#!/usr/bin/python

import sys
import re

outputFile = open('inverted-index.txt', 'w')
firstLine = True
for inputLine in sys.stdin:
    if not firstLine:
        line = inputLine.split(',')
        businessId = line[0]
        allBusinesses = line[-1]
        businesses = allBusinesses.split(";")
        for i in range(len(businesses)):
            outputFile.write(str.rstrip(businesses[i]) + '\t' + str(businessId) + '\n')


    else:
        firstLine = False