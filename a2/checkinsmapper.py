#!/usr/bin/python

import re
import csv

outputFile = open('checkinsbyday.txt', 'w')

with open('yelp_checkin.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        line = re.sub(r'^\W+|\W+$', '', row[0])
        business = row[3]
        day = row[1]

        outputFile.write(business + ', ' + day + + '\t1' + '\n')
