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

avgStars = data.loc[data['city'] == cityName].stars.mean()
print(avgStars)

restaurantCategory = data.loc[data['categories'].str.contains('Restaurants')]
numOfRestaurants = restaurantCategory.loc[data['city'] == cityName].city.count()
print(numOfRestaurants)

restaurantCategory = data.loc[data['categories'].str.contains('Restaurants')]
avgStarsRestaurants = restaurantCategory.loc[data['city'] == cityName].stars.mean()
print(avgStarsRestaurants)

avgNumOfReviews = data.loc[data['city'] == cityName].review_count.mean()
print(avgNumOfReviews)

restaurantCategory = data.loc[data['categories'].str.contains('Restaurants')]
avgNumOfReviewsBus = restaurantCategory.loc[data['city'] == cityName].review_count.mean()
print(avgNumOfReviewsBus)
