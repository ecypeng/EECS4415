import sys
import re
import csv

# numUnigram = 0

# outputFile = open('unigrams.txt', 'r')
# # outputFile1 = open('unigrams.txt', 'w')

# # lines = outputFile.readlines()
# # lines.sort()

# for row in outputFile:
#     # outputFile1.write(row)
#     numUnigram = numUnigram + 1

# print(str(numUnigram))

with open('unigrams.txt', 'r') as file:
    for line in sorted(file):
        print(line, end='')
