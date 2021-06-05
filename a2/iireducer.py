#!/usr/bin/python

import sys

previous = None
sum = 0

for line in sys.stdin:
    busCat, busId = line.split('\t')
    if busCat != previous:
        if previous is not None:
            print(str(busCat) + ', ' + str(sum))
        previous = busCat
        sum = 0
    sum = sum + int(value)
    
print(str(busCat) + ', ' + str(sum))