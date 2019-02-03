from textblob import TextBlob
import pandas as pd
import json
import os

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


    return json.dumps(x1)

# os.chdir("../")
# os.chdir("../")
#


# with open('jsonfile.json', 'w') as outfile:
#     json.dump(x1, outfile, indent =4)





