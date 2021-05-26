import sys
import pandas
import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# store command line arguements as variables
targetFile = sys.argv[1]
cityName = sys.argv[2]
categoryFrequency = {}
reviews = {}
starsTotal = {}
starsCount = {}
reviewStats = {}
genericRestaurantCategories = ['Restaurants', 'Seafood', 'Food', 'Bars', 'Nightlife']
# https://www.programiz.com/python-programming/reading-csv-files
with open(targetFile, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        businessCategories = []
        if row[4] == cityName and 'Restaurant' in row[12]:
            businessCategories = str(row[12]).split(';')
            for cat in range(len(businessCategories)):
                if businessCategories[cat] not in genericRestaurantCategories:
                    if businessCategories[cat] not in categoryFrequency.keys():
                        categoryFrequency[businessCategories[cat]] = 1
                    else:
                            categoryFrequency[businessCategories[cat]] += 1
                    if businessCategories[cat] not in reviews.keys():
                        reviews[businessCategories[cat]] = int(row[10])
                    else:
                        reviews[businessCategories[cat]] += int(row[10])
                    if businessCategories[cat] not in starsTotal.keys():
                        starsTotal[businessCategories[cat]] = float(row[9])
                    else:
                        starsTotal[businessCategories[cat]] += float(row[9])
                    if businessCategories[cat] not in starsCount.keys():
                        starsCount[businessCategories[cat]] = 1
                    else:
                        starsCount[businessCategories[cat]] += 1

# sorting dict by value descending to match requirements
# source: https://thispointer.com/sort-a-dictionary-by-value-in-python-in-descending-ascending-order/#:~:text=sorted%20by%20value.-,Sort%20the%20dictionary%20by%20value%20in%20descending%20order%20using%20itemgetter,but%20in%20descending%20order%20i.e.
sortedCategoryFrequency = dict( sorted(categoryFrequency.items(),
                           key=lambda item: item[1],
                           reverse=True))

sortedReviews = dict( sorted(reviews.items(),
                           key=lambda item: item[1],
                           reverse=True))

# #print all keys and values
for i, j in sortedCategoryFrequency.items():
    print (i + ":" + str(j))

for name, reviews in reviews.items():
    reviewStats[name] = str(name) + ":" + str(sortedReviews.get(name)) + ":" + str(starsTotal.get(name)/starsCount.get(name))

sortedReviewStats = dict( sorted(reviewStats.items(),
                           key=lambda item: item[1],
                           ))

for i, j in sortedReviewStats.items():
    print (str(j))

sortedCategoryFrequencyValues = []
#getting values for graph
for i, j in sortedCategoryFrequency.items():
    sortedCategoryFrequencyValues.append(j)
sortedCategoryFrequencyValues = sortedCategoryFrequencyValues[:10]

# https://pythonspot.com/matplotlib-bar-chart/
objects = (list(sortedCategoryFrequency)[0], list(sortedCategoryFrequency)[1], list(sortedCategoryFrequency)[2],  list(sortedCategoryFrequency)[3], list(sortedCategoryFrequency)[4], list(sortedCategoryFrequency)[5], 
list(sortedCategoryFrequency)[6], list(sortedCategoryFrequency)[7], list(sortedCategoryFrequency)[8], list(sortedCategoryFrequency)[9])
y_pos = np.arange(len(objects))
performance = sortedCategoryFrequencyValues

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('category')
plt.ylabel('#restaurants')
plt.title('frequency distribution of the number of restaurants in each category of restaurants')

plt.show()