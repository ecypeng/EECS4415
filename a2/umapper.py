import re
import csv

outputFile = open('unigrams.txt', 'w')
allWords = []
with open('yelp_tip.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        line = re.sub(r'\W+|\W+$', '', row[0])
        words = re.split(r'\W+', row[0])
        for word in words:
            allWords.append(word.lower())
    
allWords.sort()    
for i in range(len(allWords)):
    outputFile.write(allWords[i] + "\t1\n")

