"""
    This Spark app connects to a script running on another (Docker) machine
    on port 9009 that provides a stream of raw tweets text. That stream is
    meant to be read and processed here, where top trending hashtags are
    identified. Both apps are designed to be run in Docker containers.

    To execute this in a Docker container, do:
    
        docker run -it -v $PWD:/app --link twitter:twitter eecsyorku/eecs4415

    and inside the docker:

        spark-submit spark_app.py

    For more instructions on how to run, refer to final tutorial 8 slides.

    Made for: EECS 4415 - Big Data Systems (York University EECS dept.)
    Modified by: Tilemachos Pechlivanoglou
    Based on: https://www.toptal.com/apache/apache-spark-streaming-twitter
    Original author: Hanee' Medhat

"""
#!/usr/bin/python
# coding=utf-8

import re
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row,SQLContext
import sys
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


# create spark configuration
conf = SparkConf()
conf.setAppName("TwitterStreamApp")
# create spark context with the above configuration
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
# create the Streaming Context from spark context, interval size 2 seconds
ssc = StreamingContext(sc, 2)
# setting a checkpoint for RDD recovery (necessary for updateStateByKey)
ssc.checkpoint("checkpoint_TwitterApp")
# read data from port 9009
dataStream = ssc.socketTextStream("twitter",9009)

# reminder - lambda functions are just anonymous functions in one line:
#
#   words.flatMap(lambda line: line.split(" "))
#
# is exactly equivalent to
#
#    def space_split(line):
#        return line.split(" ")
#
#    words.filter(space_split)

# split each tweet into words
words = dataStream.flatMap(lambda line: line.split(" "))

topics = ['#basketball', '#baseball', '#soccer', '#football', '#tennis']
basketball = ['#dribble', '#jordan', '#NBA', '#pistons', '#raptors', '#LakersNation', '#shaq', '#BrooklynNets', '#wade', '#lebron']
baseball = ['#homebase', '#homerun', '#doubleplay', '#bluejays', '#flyout', '#pitcher', '#batter', '#MLB', '#kershaw', '#ruth']
soccer = ['#goalkeeper', '#midfielder', '#ronaldo', '#liverpool', '#salah', '#MLS', '#messi', '#neymar', '#goal', '#goalie']
football = ['#touchdown', '#NFL', '#DetroitLions', '#ChicagoBears', '#NewYorkGiants', '#receiver', '#kicker', '#defense', '#MinnesotaVikings', '#tombrady']
tennis = ['#williams', '#racket', '#grandslam', '#NTL', '#rosewall', '#tenniscourt', '#tennisball', '#deuce', '#ace', '#let']

sport_hashtags = basketball + baseball + soccer + football + tennis

# filter the words to get only hashtags
hashtags = words.filter(lambda w: w in sport_hashtags)

def clean_input(tweet):
    clean = re.sub(r'[\'\d]', '', tweet)
    return clean

# def tag_filter(line):
#     res = False
#     for word in line.split(" "):
#         for hashtag in sport_hashtags:
#             if word.lower() in hashtag:
#                 res = True
#     return(res)

# hashtags = dataStream.filter(tag_filter)

def find_topic(input):
    input = clean_input(input)
    for word in input.split(" "):
        if word in basketball:
            return topics[0]
        if word in baseball:
            return topics[1]
        if word in soccer:
            return topics[2]
        if word in football:
            return topics[3]
        if word in tennis:
            return topics[4]

def sentiment(tweet):
    tweet = clean_input(tweet)
    polarity = sia.polarity_scores(tweet)

    if polarity['compound'] < 0:
        # print('negative')
        return('negative')
    elif polarity['compound'] > 0:
        # print('positive')
        return('positive')
    else:
        # print('neutral')
        return('neutral')

# map each hashtag to be a pair of (hashtag,1)
hashtag_counts = hashtags.map(lambda x: (x, 1))

tweet_sentiment = words.map(lambda x: (sentiment(x), 1))

# adding the count of each hashtag to its last count
def aggregate_tags_count(new_values, total_sum):
    return sum(new_values) + (total_sum or 0)

# do the aggregation, note that now this is a sequence of RDDs
hashtag_totals = hashtag_counts.updateStateByKey(aggregate_tags_count)

# process a single time interval
def process_interval(time, rdd):
    # print a separator
    print("----------- %s -----------" % str(time))
    try:
        # sort counts (desc) in this time instance and take top 10
        sorted_rdd = rdd.sortBy(lambda x:x[1], False)
        top10 = sorted_rdd.take(10)

        # print it nicely
        for tag in top10:
            print('{:<40} {}'.format(tag[0], tag[1]))
    except:
        e = sys.exc_info()[0]
        print("Error: %s" % e)

# do this for every single interval
hashtag_totals.foreachRDD(process_interval)
# tweet_sentiment.foreachRDD(process_interval)



# start the streaming computation
ssc.start()
# wait for the streaming to finish
ssc.awaitTermination()