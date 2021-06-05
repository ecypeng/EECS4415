#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    # used REGEX to split by words
    line = re.sub(r'^\W+|\W+$', '', row[0])
    words = re.split(r'\W+', line)

    for word in words:
        # lower and ouput words
        word = word.lower()
        print(word + '\t1')
