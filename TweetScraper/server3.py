import flask
from flask import Flask
from flask_cors import CORS
from textblob import TextBlob
import pandas as pd
import json
import requests
import os
import sys
import glob

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def get_review():
    data = flask.request.get_json("data")
    line = data['data']
    os.system("python3 FILE_RESETTER.py")

    for i in range(1, 9):
        line = line + " since:2018-0" + str(i) + "-01 until:2018-0" + str((i + 1) % 12) + "-01'"
        os.system("scrapy crawl TweetScraper -a query=' " + line)
        exporting(i)

    i = 9
    line = line + " since:2018-0" + str(i) + "-01 until:2018-" + str((i + 1) % 12) + "-01'"
    os.system("scrapy crawl TweetScraper -a query=' " + line)
    exporting(i)
    for i in range(10, 12):
        line = line + " since:2018-" + str(i) + "-01 until:2018-" + str(i + 1) + "-01'"
        os.system("scrapy crawl TweetScraper -a query=' " + line)
        exporting(i)

    # os.system("scrapy crawl TweetScraper -a query='" + line + " since:2019-01-01 until:2019-02-02'")
    #os.system("python3 ExportingIsFUN.py")
    # os.system("python3 sentiment.py")

    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT,  'jsonfile.json')
    # data = json.load(open(json_url))

    with open('data1.csv','a') as singleFile:
        for csv in glob('*.csv'):
            if csv == 'main.csv':
                pass
            else:
                for line in open(csv, 'r'):
                    singleFile.write(line)


    return sent_func()
    # return it lol


def sent_func():
    os.chdir("Data/tweet")
    data = pd.read_csv("data1.csv")
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
    return json.dumps(x1, indent=4)



def exporting(i):
    print(os.getcwd())
    os.chdir("Data/tweet")

    print(os.getcwd())
    # print(os.listdir())

    files = os.listdir()
    print(files)

    dict = []

    for file in files:
        if (file != '.DS_Store' and file!='data1.csv' and file!='data2.csv'): #Additional files to be ignored rn
            print('i is ' + str(i))
            json_string = open(file, 'r', encoding="latin-1").read()
            json_dict = json.loads(json_string)
            dict.append(json_dict)


    df = pd.DataFrame(dict)
    df = df.replace({'\n': ' '}, regex=True)  # remove linebreaks in the dataframe
    df = df.replace({'\t': ' '}, regex=True)  # remove tabs in the dataframe
    df = df.replace({'\r': ' '}, regex=True)  # remove carriage return in the dataframe

    df

    # Export to csv
    filename = "data" + str(i) + ".csv"
    df.to_csv(filename)
    print("The tweets are now in a CSV! :D")



if __name__ == "__main__":
    app.run()
