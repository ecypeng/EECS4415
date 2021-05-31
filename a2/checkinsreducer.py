#!/usr/bin/python

previous = None
sum = 0

file = open('checkinsbyday.txt', 'r')

for line in file:
        key, value = line.split('\t')

        if key != previous:
                if previous is not None:
                        print(str(sum) + ', ' + previous)
                previous = key
                sum = 0
        sum = sum + int(value)
print(str(sum) + ', ' + previous)