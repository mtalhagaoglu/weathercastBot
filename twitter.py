import tweepy
import json
import random
import os.path

with open("secret.json") as json_data_file:
    data = json.load(json_data_file)

consumer_key = data["tw_consumer_key"]
consumer_secret = data["tw_consumer_secret"]
access_token = data["tw_access_token"]
access_token_secret = data["tw_access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def sendDailyTweet(status,hour):
    print(status)
    if int(hour) < 12:
        kindWord = "Günaydın"
    else:
        kindWord = "İyi akşamlar"
    if random.choice([0,0,1]):
        print("Funny text")
        id = status["weather"][0]["id"]
        if(id == 800):
            if os.path.isfile("templates/800.txt"):
                file = open("templates/{}xx.txt", "r")
                arrayOfLines = file.readlines()
                funnyWord = random.choice(arrayOfLines)
        else:
            id = int(round(id/100,1))
            if os.path.isfile('templates/{}xx.txt'.format(id)):
                file = open("templates/{}xx.txt".format(id),"r")
                arrayOfLines = file.readlines()
                funnyWord = random.choice(arrayOfLines)
    else:
        print("not funny word")
        funnyWord = ""
    tweet = "{}!\nBugün hava {} ve {} derece!\n{}".format(kindWord,status["weather"][0]["description"],status["feels_like"]["day"],funnyWord)
    print(tweet)
    api.update_status(status=tweet)

def sendRainAlarm(status):
    tweet = "Dikkat! Bir saat sonra yağmur yağabilir!"
    print(tweet)
    api.update_status(status=tweet)