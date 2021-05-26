import csv
import sys
import pandas

# store command line arguements as variables
targetFile = sys.argv[1]
cityName = sys.argv[2]

# get the target CSV file
data = pandas.read_csv(targetFile)

# getting the city that was entered in the command line and getting the count
numOfBus = data.loc[data['city'] == cityName].city.count()
print(numOfBus)

# getting the city that was entered in the command line and getting the mean of their stars
avgStars = data.loc[data['city'] == cityName].stars.mean()
print(avgStars)

# getting the categories that contain Restaurants
restaurantCategory = data.loc[data['categories'].str.contains('Restaurants')]

# getting the restuarants in the city that was enterd in the command line and getting its count
numOfRestaurants = restaurantCategory.loc[data['city'] == cityName].city.count()
print(numOfRestaurants)

# calculating the average stars by getting the city that was entered in the command line and getting the mean of their stars
avgStarsRestaurants = restaurantCategory.loc[data['city'] == cityName].stars.mean()
print(avgStarsRestaurants)

# getting the city entered in the command line and getting the average of the review_count
avgNumOfReviews = data.loc[data['city'] == cityName].review_count.mean()
print(avgNumOfReviews)

# getting the city that was entered in the command line and getting the average review_count
avgNumOfReviewsBus = restaurantCategory.loc[data['city'] == cityName].review_count.mean()
print(avgNumOfReviewsBus)
