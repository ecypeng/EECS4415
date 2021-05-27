import sys
import re

targetFile = open('yelp_tip.csv', 'r')
outputFile = open('unigrams.txt', 'w')

for line in sys.stdin:
    line = re.sub( r'\W+|\W+$', '', line )
    words = re.split(r'\W+', line)

    for word in words:
        word = word.lower()
        outputFile.write(word + "\n")
