#!/usr/bin/python

import sys

previous = None
sum = 0

for line in sys.stdin:
    # split by key value variables
    key, value = line.split('\t')

    if key != previous:
        if previous is not None:
            # if key is not previous and is not none, then ouput
            print(str(sum) + '\t' + previous)
        # reset previous and sum variables
        previous = key
        sum = 0
    # add to sum variable
    sum = sum + int(value)
print(str(sum) + '\t' + previous)
