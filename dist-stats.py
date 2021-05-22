import sys
import pandas
import matplotlib.pyplot as plt

# getting input from the command line
targetFile = sys.argv[1]
cityName = sys.argv[2]

def printResults(rest):
    # applying to be a str
    rest = rest.applymap(str)
    # so that in the terminal output they are all close together. so 1:2 instead of 1 : 2
    rest = rest.apply(lambda x: ':'.join(x), axis=1)
    # printing it and not showing the index
    print(rest.to_string(index=False))

# reading the contents of the file
data = pandas.read_csv(targetFile)

# getting the ones that have the cityName that was entered in the terminal
data = data[data['city'].str.contains(cityName, na=False)]
# looking through the categories and getting the ones that contain "Restaurant"
data = data[data['categories'].str.contains('Restaurant')] 

# Splitting the category by the ; and putting in a list. Getting the city and stacking
restaurant = pandas.DataFrame(data.categories.str.split(';').tolist(), index=data.city).stack()

# have to reset the index each time
restaurant = restaurant.reset_index([0, 'city'])

# this is to change the column names.
restaurant.columns = ['restaurant','category']

# Gets rid of theses categories. Because these aren't the categories we want to show. We want to show the different kinds of food categories
restaurant = restaurant.loc[~restaurant['category'].str.contains('Restaurant|Seafood|Food|Bars|Nightlife')]

# getting the number of categories
numRestaurantCategories = restaurant.groupby('category', as_index=False).count()

# getting the values and setting them to be descending
restaurantCategoryDist = numRestaurantCategories.sort_values('restaurant',ascending=False)

# printing the categories
printResults(restaurantCategoryDist)

# gets the count of categories and sorts them by their values from most to least
categoriesCount = restaurant.groupby('category').count()
restaurantBarSize = categoriesCount.sort_values('restaurant',ascending=False)

# Splitting the category by the ; and putting in a list. Getting the city and stacking
restaurant = pandas.DataFrame(data.categories.str.split(';').tolist(), index=data.business_id).stack()

# have to reset the index each time
restaurant = restaurant.reset_index([0, 'business_id'])

# merge the restaurant data
restaurant = data.merge(restaurant)

restaurant.rename(columns={restaurant.columns[-1]: 'category'}, inplace = True)

# aggregage
restaurant = restaurant.groupby('category', as_index=False).agg(
{
'categories':'count',
'review_count':sum,
'stars':'mean'
})

# setting the columns
restaurant.columns = ['category', 'restaurant', 'reviews', 'averageStars']

# to only print these three
restaurant = restaurant[['category', 'reviews', 'averageStars']]

# sorting by most reviews to least
restaurantCategoryDist = restaurant.sort_values('reviews', ascending=False)

# Gets rid of theses categories
restaurant = restaurant.loc[~restaurant['category'].str.contains('Restaurants|Seafood|Food|Bars|Nightlife')]

# print
printResults(restaurantCategoryDist)


# so that it shows the top 10
numBarsOnGraph = restaurantBarSize[:10]

# below is to plot the bar graph
axis = numBarsOnGraph[['restaurant']].plot(kind='bar', title='frequency distribution of the number of restaurants in each category of restaurants', legend=True, fontsize=10)
axis.set_xlabel('category', fontsize=12)
axis.set_ylabel('#restaurants', fontsize=12)
# Makes the whole bar graph show. Without this it's too zoomed in and can't see all the lables
plt.tight_layout()
# actually show the graph
plt.show()
