#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    # used REGEX to split by words
    line = re.sub(r'^\W+|\W+$', '', row[0])
    words = re.split(r'\W+', line)

    # created 3 word ngrams
    ngrams = zip(*[words[i:] for i in range(3)])

    # added spaces and output triples
    for triple in ngrams:
        word = ' '.join(triple).lower()
        print(word + '\t1')
