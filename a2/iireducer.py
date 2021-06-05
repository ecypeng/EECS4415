#!/usr/bin/python

import sys

previous = None
sum = []
formattedString = ''

for line in sys.stdin:
    # split by category and id
    busCat, busId = line.split('\t')

    # if the category is same as the previous
    if busCat != previous:
        # and is not the first
        if previous is not None:
            # this for loop iterates through each value except the last one to append commas
            for i in range(len(sum)-1):
                formattedString += sum[i]
                formattedString += ", "
                # append final value
            formattedString += sum[-1]
            print(str(previous) + '\t' + formattedString)

        # reset value of previous and sum
        previous = busCat
        sum = []

    sum.append(str.rstrip(busId))

    formattedString = ''
    for i in range(len(sum)-1):
        formattedString += sum[i]
        formattedString += ", "
    formattedString += sum[-1]

print(str(previous) + ', ' + formattedString)