#!/usr/bin/python

import sys

firstLine = True
for inputLine in sys.stdin:
    # boolean check for first line
    if not firstLine:
        # split value by commans
        line = inputLine.split(',')
        # grab id from first column
        businessId = line[0]
        # grab all businesses from last column
        allBusinesses = line[-1]
        # split businesses by ';'
        businesses = allBusinesses.split(";")
        for i in range(len(businesses)):
            # remove \n's and concatenate string for output
            print(str.rstrip(businesses[i]) + '\t' + str(businessId))
    else:
        # set boolean to false after first line
        firstLine = False