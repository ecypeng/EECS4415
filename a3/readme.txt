Part A:
To run this, first open three terminal windows.

In terminal window 1, please follow these steps:
1. docker run -it -v $PWD:/app --name twitter -w /app python bash
2. pip install tweepy
3. python twitter_app_a.py

In terminal window 2, please follow these steps:
1. docker run -it -v $PWD:/app --link twitter:twitter eecsyorku/eecs4415
2. spark-submit spark_app_a.py

In terminal window 3, please run:
1. python graph_a.py

You will now see the code and graph running.

Part B:
To run this, first open three terminal windows.

In terminal window 1, please follow these steps:
1. docker run -it -v $PWD:/app --name twitter -w /app python bash
2. pip install tweepy
3. python twitter_app_b.py

In terminal window 2, please follow these steps:
1. docker run -it -v $PWD:/app --link twitter:twitter eecsyorku/eecs4415
2. apt-get update -y
3. apt-get install gcc -y
4. apt-get install python3-dev -y
5. pip install nltk
7. spark-submit spark_app_b.py

In terminal window 3, please run:
1. python graph_b.py

You will now see the code and graph running.
