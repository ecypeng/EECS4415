Part A:
To run this, first open two terminal windows.

In terminal window 1, please follow these steps:
1. docker run -it -v $PWD:/app --name twitter -w /app python bash
2. pip install tweepy
3. python twitter_app_a.py

In terminal window 2, please follow these steps:
1. docker run -it -v $PWD:/app --link twitter:twitter eecsyorku/eecs4415
2. spark-submit spark_app_a.py

You will now see the code running.

Part B:
To run this, first open two terminal windows.

In terminal window 1, please follow these steps:
1. docker run -it -v $PWD:/app --name twitter -w /app python bash
2. pip install tweepy
3. python twitter_app_b.py

In terminal window 2, please follow these steps:
1. docker run -it -v $PWD:/app --link twitter:twitter eecsyorku/eecs4415
2. export PYSPARK_PYTHON=python3.5
3. apt-get update
4. apt-get install gcc

# apt-get update -y
# apt-get install gcc -y
# apt-get install python3-dev -y
python
    import nltk
    nltk.download('vader_lexicon')

5. apt-get install python-dev python3-dev
6. pip install nltk
7. spark-submit spark_app_b.py

