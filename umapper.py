import sys
import re
import csv

outputFile = open('unigrams.txt', 'w')

with open('yelp_tip.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])
        line = re.sub(r'\W+|\W+$', '', row[0])
        words = re.split(r'\W+', row[0])

        for word in words:
            word = word.lower()
            outputFile.write(word + "\t1" + "\n")
