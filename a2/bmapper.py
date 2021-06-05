#!/usr/bin/python

import sys
import re
import csv

# https://albertauyeung.github.io/2018/06/03/generating-ngrams.html
# https://www.datacamp.com/community/tutorials/case-conversion-python

reader = csv.reader(sys.stdin)
for row in reader:
    # using REGEX to isolate for each individual line, then each word
    line = re.sub(r'^\W+|\W+$', '', row[0])
    words = re.split(r'\W+', line)

    # zip the words to create ngrams
    ngrams = zip(*[words[i:] for i in range(2)])

    # join back the tuple and lower any uppercases
    for tuple in ngrams:
        line = ' '.join(tuple).lower()
        print(line + '\t1')