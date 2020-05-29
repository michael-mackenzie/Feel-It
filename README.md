## Scraping Tweets

TweetScraper can get tweets from Twitter Search. It is built on Scrapy without using Twitter's APIs. The crawled data is not as clean as the one obtained by the APIs, but the benefit is you can get rid of the API's rate limits and restrictions. Ideally, you can get all the data from Twitter Search.


## Sentiment Analysis

Sentiment analysis was done using textblob.
From their documentation: TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

Textblob gives us a value in the range -1 to 1 representing how positive a tweet is. A value of -1 means the tweet is speaking negatively about your query and a value of 1 means the tweet is speaking positively about your query.


This was made at Qhacks 2019!
Check out our devpost: https://devpost.com/software/how-do-you-feel-h1ajyc!
