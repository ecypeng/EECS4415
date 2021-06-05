#!/usr/bin/python

import sys
import csv

# variable to check if the value is the first value
count = 0

reader = csv.reader(sys.stdin)
for row in reader:
    if count == 1:
        # store relevant data from line input
        businessId = row[0]
        dayOfWeek = row[1]
        checkins = row[3]
        print(businessId + ', ' + dayOfWeek + '\t' + checkins)
    # set count to 1 after first input line
    count = 1
