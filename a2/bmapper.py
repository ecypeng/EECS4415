#!/usr/bin/python

import re
import csv

# https://albertauyeung.github.io/2018/06/03/generating-ngrams.html
# https://www.datacamp.com/community/tutorials/case-conversion-python

outputFile = open('bigrams.txt', 'w')

with open('yelp_tip.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])
        line = re.sub(r'\W+|\W+$', '', row[0])
        words = re.split(r'\W+', row[0])

        # for word in words:
        #     word = word.lower()

        # ngram = zip(*[words[i:] for i in range(2)])

        ngrams = zip(*[words[i:] for i in range(2)])

        tuple = [" ".join(ngram).lower() for ngram in ngrams]
        [outputFile.write(''.join(t) + '\t1' + '\n') for t in tuple]

        # for tuple in ngrams:
        #     line = ' '.join(tuple).lower()
        #     outputFile.write(line + '\t1' + '\n')

# outputFile = open('bigrams.txt', 'w')
# allWords = []

# with open('yelp_tip.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[0])
#         line = re.sub(r'\W+|\W+$', '', row[0])
#         words = re.split(r'\W+', row[0])
#         # for word in words:
#         #     allWords.append(word.lower())

#         ngrams = zip(*[words[i:] for i in range(2)])

#         for ngram in ngrams:
#             tuple = " ".join(ngram).lower()
#             for word in tuple:
#                 allWords.append(word.lower())
#         allWords.sort()
#         [outputFile.write(allWords[t] + '\t1' + '\n') for t in tuple]

#         # allWords.sort()
#         # for tuple in ngrams:
#         #     line = ' '.join(tuple).lower()
#         #     outputFile.write(line + '\t1' + '\n')
