# import flask
# from flask import Flask
# from flask_cors import CORS
# from textblob import TextBlob
# import pandas as pd
# import json
# import requests
# import os
# import sys
#
#
# app = Flask(__name__)
# CORS(app)
#
# @app.route("/", methods=["POST"])
# def get_review():
#     data = flask.request.get_json("data")
#     line = data['data']
#     os.system("python3 FILE_RESETTER.py")
#     os.system("scrapy crawl TweetScraper -a query='" + line + " since:2019-01-01 until:2019-02-02'")
#     os.system("python3 ExportingIsFUN.py")
#     #os.system("python3 sentiment.py")
#
#     # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#     # json_url = os.path.join(SITE_ROOT,  'jsonfile.json')
#     # data = json.load(open(json_url))
#
#     return sent_func()
#     #return it lol
#
# def sent_func():
#     os.chdir("Data/tweet")
#     data = pd.read_csv("data.csv")
#     text = data.text.tolist()
#     date = data.datetime.tolist()
#
#     for i in range(len(date)):
#         date[i] = pd.to_datetime(date[i]).date()
#     x1 = []
#     for i in range(len(text)):
#         polar = TextBlob(text[i]).sentiment.polarity
#         subject = TextBlob(text[i]).sentiment.subjectivity
#         if polar > 0:
#             posneg = 'positive'
#         elif polar == 0:
#             posneg = 'neutral'
#         else:
#             posneg = 'negative'
#         x1.append({"date": str(date[i]), "text": text[i], "polarity": polar, "sign": posneg, "subjectivity": subject})
#
#     os.chdir("../../")
#     return json.dumps(x1, indent =4)
#
# if __name__ == "__main__":
#     app.run()


import flask
from flask import Flask
from flask_cors import CORS
from textblob import TextBlob
import pandas as pd
import json
import requests
import os
import sys


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def get_review():
    data = flask.request.get_json("data")
    line = data['data']
    os.system("python3 FILE_RESETTER.py")
    os.system("scrapy crawl TweetScraper -a query='" + line + " since:2019-01-01 until:2019-02-02'")
    os.system("python3 ExportingIsFUN.py")
    #os.system("python3 sentiment.py")

    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT,  'jsonfile.json')
    # data = json.load(open(json_url))

    return sent_func()
    #return it lol

def sent_func():
    os.chdir("Data/tweet")
    data = pd.read_csv("data.csv")
    text = data.text.tolist()
    date = data.datetime.tolist()

    for i in range(len(date)):
        date[i] = pd.to_datetime(date[i]).date()
    x1 = []
    for i in range(len(text)):
        polar = TextBlob(text[i]).sentiment.polarity
        subject = TextBlob(text[i]).sentiment.subjectivity
        if polar > 0:
            posneg = 'positive'
        elif polar == 0:
            posneg = 'neutral'
        else:
            posneg = 'negative'
        x1.append({"date": str(date[i]), "text": text[i], "polarity": polar, "sign": posneg, "subjectivity": subject})

    os.chdir("../../")
    return json.dumps(x1, indent =4)

if __name__ == "__main__":
    app.run()
