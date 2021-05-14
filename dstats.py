import csv
import sys
import pandas

# store command line arguements as variables
targetFile = sys.argv[1]
cityName = sys.argv[2]

# get the target CSV file
data = pandas.read_csv(targetFile)

numOfBus = data.loc[data['city'] == cityName].city.count()
print(numOfBus)
