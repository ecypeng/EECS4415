#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    line = re.sub(r'^\W+|\W+$', '', row[0])
    words = re.split(r'\W+', line)

    ngrams = zip(*[words[i:] for i in range(3)])

    for triple in ngrams:
        word = ' '.join(triple).lower()
        print(word + '\t1')
