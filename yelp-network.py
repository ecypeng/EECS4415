import csv
import sys
import pandas

# store command line arguement as variable
targetFile = sys.argv[1]

# get the target CSV file
data = pandas.read_csv(targetFile)
f = open("yelp-network.txt", "w")
textList = ["One", "Two", "Three", "Four", "Five"]
for line in textList:
  # write line to output file
  f.write(line)
  f.write("\n")
f.close()