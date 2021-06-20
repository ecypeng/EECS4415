# import nltk
import re
# nltk.download('vader_lexicon')
# from nltk.sentiment import SentimentIntensityAnalyzer

# sia = SentimentIntensityAnalyzer()


# def clean_input(tweet):
#     clean = re.sub(r'^\W+|\W+$', '', tweet)
#     return clean

def clean_input(input):
 # next, the input must be stripped of punctuation excluding hashtags since we need them
    # temp = re.sub(r'[^\w#]', ' ', input)

    # now, any contractions are collapsed by removing the apostrophes
    # temp = re.sub(r'[\']', '', input)
    
    # any numbers will also be removed since they hold very little meaning later on
    temp = re.sub(r'[\'\d]', '', input)

    # replace all whitespace with the space character, this joins all the text into one scenetence
    # temp = re.sub(r'[\s]', ' ', temp)
    return temp

# def sentiment(tweet):
#     tweet = clean_input(tweet)
#     polarity = sia.polarity_scores(tweet)

#     if polarity['compound'] > 0:
#         print('negative')
#         return(1)
#     elif polarity['compound'] < 0:
#         print('positive')
#         return(-1)
#     else:
#         print('neutral')
#         return(0)

print(clean_input('#!,hell\'o my nam\'e is, is 222'))
