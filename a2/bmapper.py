#!/usr/bin/python

import sys
import re
import csv

# https://albertauyeung.github.io/2018/06/03/generating-ngrams.html
# https://www.datacamp.com/community/tutorials/case-conversion-python

reader = csv.reader(sys.stdin)
for row in reader:
    line = re.sub(r'^\W+|\W+$', '', row[0])
    words = re.split(r'\W+', line)

    # for word in words:
    #     word = word.lower()

    # ngram = zip(*[words[i:] for i in range(2)])

    ngrams = zip(*[words[i:] for i in range(2)])

    tuple = [" ".join(ngram).lower() for ngram in ngrams]
    # [outputFile.write(''.join(t) + '\t1' + '\n') for t in tuple]

    for tuple in ngrams:
        line = ' '.join(tuple).lower()
        print(line + '\t1')