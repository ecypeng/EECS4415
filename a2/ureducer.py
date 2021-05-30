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

# with open('unigrams.txt', 'r') as file:
#     for line in sorted(file):
#         print(line, end='')

# import sys

# previous = None
# sum = 0

# for line in sys.stdin:
#     key, value = line.split('\t')

#     if key != previous:
#         if previous is not None:
#             print(str(sum) + '\t' + previous)
#         previous = key
#         sum = 0

#     sum = sum + int(value)
# print(str(sum) + '\t' + previous)

import sys

previous = None
sum = 0

file = open('unigrams.txt', 'r')

for line in file:
    key, value = line.split('\t')

    if key != previous:
        if previous is not None:
            print(str(sum) + '\t' + previous)
        previous = key
        sum = 0

    sum = sum + int(value)
print(str(sum) + '\t' + previous)
