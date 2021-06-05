#!/usr/bin/python

import sys

previous = None
sum = 0

for line in sys.stdin:
    # split by tab and store in key value pairs
    key, value = line.split('\t')

    if key != previous:
        if previous is not None:
            # output if key is not previous and is not none
            print(str(sum) + '\t' + previous)
        # set values to previous and sum
        previous = key
        sum = 0

    # increment value of sum
    sum = sum + int(value)
print(str(sum) + '\t' + previous)
