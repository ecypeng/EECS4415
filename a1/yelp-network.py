import sys
import pandas
import numpy

# store command line arguement as variable
targetFile = sys.argv[1]

# get the target CSV file
data = pandas.read_csv(targetFile)

# filter out rows without friends
data = data[~data['friends'].str.contains('None')]
# splitting by , and stacking
friendPairing = pandas.DataFrame(data.friends.str.split(',').tolist(), index = data.user_id).stack()
# reset the index
friendPairing = friendPairing.reset_index([0, 'user_id'])
# setting the column names
friendPairing.columns = ['friend1ID', 'friend2ID']

# checking for duplicates + reverse duplicates
noDuplicates = pandas.DataFrame(numpy.sort(friendPairing.values, axis = 1), columns = friendPairing.columns).drop_duplicates()

with open('yelp-network.txt', 'w') as myfile:
  noDuplicates.to_csv(myfile, header= None, index = False)

# reading the contents of yelp-network.txt
f = open("yelp-network.txt", "r")
# reading the contents of yelp-network.txt and setting it to data1
data1 = f.read()
# replacing all spaces with nothing (so removing spaces) and replacing all , with spaces
data1 = data1.replace(' ', '')
data1 = data1.replace(',', ' ')
# close the file yelp-network.txt
f.close()
# opening yelp-network.txt to write to it
f = open("yelp-network.txt", "w")
# writing the contents of data1 to yelp-network.txt
f.write(data1)
# close the file yelp-network.txt
f.close()
