#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    line = re.sub(r'^\W+|\W+$', '', row[0])
    # print(line)
    words = re.split(r'\W+', line)
    for word in words:
        word = word.lower()
        print(word + '\t1')
