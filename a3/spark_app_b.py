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
basketball = ['#dribble', '#jordan', '#nba', '#pistons', '#raptors', '#lakersnation', '#shaq', '#brooklynnets', '#wade', '#lebron']
baseball = ['#homebase', '#homerun', '#doubleplay', '#bluejays', '#flyout', '#pitcher', '#batter', '#mlb', '#kershaw', '#ruth']
soccer = ['#goalkeeper', '#midfielder', '#ronaldo', '#liverpool', '#salah', '#mls', '#messi', '#neymar', '#goal', '#goalie']
football = ['#touchdown', '#nfl', '#detroitlions', '#chicagobears', '#newyorkgiants', '#receiver', '#kicker', '#defense', '#minnesotavikings', '#tombrady']
tennis = ['#williams', '#racket', '#grandslam', '#ntl', '#rosewall', '#tenniscourt', '#tennisball', '#deuce', '#ace', '#let']

sport_hashtags = basketball + baseball + soccer + football + tennis

# filter the words to get only hashtags
# hashtags = words.filter(lambda w: w in sport_hashtags)

def clean_input(tweet):
    clean = re.sub(r'[\'\d]', '', tweet)
    return clean

def tag_filter(line):
    containsHashtag = False
    for word in line.split(" "):
        for hashtag in sport_hashtags:
            if word.lower() in hashtag:
                containsHashtag = True
    return(containsHashtag)

hashtags = dataStream.filter(tag_filter)

def find_topic(input):
    return_topic = ""
    input_clean = clean_input(input)
    full_tweet = input_clean.split(" ")
    for word in full_tweet:
        if word in basketball:
            return_topic = topics[0]
        if word in baseball:
            return_topic = topics[1]
        if word in soccer:
            return_topic = topics[2]
        if word in football:
            return_topic = topics[3]
        if word in tennis:
            return_topic = topics[4]
    return return_topic


def sentiment(tweet):
    tweet = clean_input(tweet)
    polarity = sia.polarity_scores(tweet)
    sent = ''
    if (find_topic(tweet) != ""):
        if polarity['compound'] < 0:
            sent = 'negative'
        elif polarity['compound'] > 0:
            sent = 'positive'
        else:
            sent = 'neutral'
    return sent

# map each hashtag to be a pair of (hashtag,1)
hashtag_counts = hashtags.map(lambda x: (find_topic(x) + " " + sentiment(x), 1 if sentiment(x) != '' else 0))

# adding the count of each hashtag to its last count
def aggregate_tags_count(new_values, total_sum):
    return sum(new_values) + (total_sum or 0)

# do the aggregation, note that now this is a sequence of RDDs
hashtag_totals = hashtag_counts.updateStateByKey(aggregate_tags_count)
graph_info = open('graph_info_b.txt', 'a+')
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
            graph_info.write('{:<40} {}\n'.format(tag[0], tag[1])) 
    except:
        e = sys.exc_info()[0]
        print("Error: %s" % e)

# do this for every single interval
hashtag_totals.foreachRDD(process_interval)

# start the streaming computation
ssc.start()
# wait for the streaming to finish
ssc.awaitTermination()