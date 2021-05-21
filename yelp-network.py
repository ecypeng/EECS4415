import csv
import sys
import pandas
import numpy

# store command line arguement as variable
targetFile = sys.argv[1]

# get the target CSV file
data = pandas.read_csv(targetFile)

# filter out rows without friends
data = data[~data['friends'].str.contains('None')]
friendPairing = pandas.DataFrame(data.friends.str.split(',').tolist(), index = data.user_id).stack()
friendPairing = friendPairing.reset_index([0, 'user_id'])
friendPairing.columns = ['friend1ID', 'friend2ID']

# checking for duplicates + reverse duplicates
something = pandas.DataFrame(numpy.sort(friendPairing.values, axis = 1), columns = friendPairing.columns).drop_duplicates()

with open('yelp-network.txt', 'w') as myfile:
  something.to_csv(myfile, header= None, index = False)

#read input file
fin = open("yelp-network.txt", "rt")
#read file contents to string
data1 = fin.read()
#replace all occurrences of the required string
data1 = data1.replace(' ', '')
data1 = data1.replace(',', ' ')
#close the input file
fin.close()
#open the input file in write mode
fin = open("yelp-network.txt", "wt")
#overrite the input file with the resulting data
fin.write(data1)
#close the file
fin.close()