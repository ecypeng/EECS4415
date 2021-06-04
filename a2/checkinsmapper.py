#!/usr/bin/python

import sys
import csv

count = 0

reader = csv.reader(sys.stdin)
for row in reader:
    if count == 1:
        businessId = row[0]
        dayOfWeek = row[1]
        checkins = row[3]
        print(businessId + ', ' + dayOfWeek + '\t' + checkins)
    count = 1
