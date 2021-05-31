#!/usr/bin/python

import re
import csv

outputFile = open('trigrams.txt', 'w')

with open('yelp_tip.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])
        line = re.sub(r'\W+|\W+$', '', row[0])
        words = re.split(r'\W+', row[0])

        ngrams = zip(*[words[i:] for i in range(3)])

        for triple in ngrams:
            line = ' '.join(triple).lower()
            outputFile.write(line + '\t1' + '\n')
