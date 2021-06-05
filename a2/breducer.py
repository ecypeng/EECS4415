#!/usr/bin/python

# this was inspired by the class tutorial slides
import sys

previous = None
sum = 0

for line in sys.stdin:
    # split by tab and store in key and value variables
    key, value = line.split('\t')

    # if the key is not the same as the previous,
    if key != previous:
        # if the key is not none
        if previous is not None:
            print(str(sum) + '\t' + previous)
        # reset the values
        previous = key
        sum = 0

    # increase the counter sum
    sum = sum + int(value)
print(str(sum) + '\t' + previous)