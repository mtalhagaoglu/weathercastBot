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
    dayWord = "Bugün"
    if int(hour) < 12:
        kindWord = "Günaydın"
        feels_like = round(status["temp"]["day"],1)
    else:
        kindWord = "İyi akşamlar"
        feels_like = round(status["temp"]["eve"],1)
        if int(hour) > 20:
            dayWord = "Yarın"
            feels_like = round(status["temp"]["day"],1)
    if random.choice([0,0,1]):
        print("Funny text")
        id = status["weather"][0]["id"]
        if(id == 800):
            if os.path.isfile("templates/800.txt"):
                file = open("templates/800.txt", "r",encoding="utf-8")
                arrayOfLines = file.readlines()
                funnyWord = random.choice(arrayOfLines)
        else:
            id = int(round(id/100,1))
            if os.path.isfile('templates/{}xx.txt'.format(id)):
                file = open("templates/{}xx.txt".format(id),"r",encoding="utf-8")
                arrayOfLines = file.readlines()
                funnyWord = random.choice(arrayOfLines)
    else:
        print("not funny word")
        funnyWord = ""
    description = status["weather"][0]["description"]
    try:
        tweet = "{}!\n{} hava {} ve sıcaklık {} derece!\n{}\n\n#HavaDurumu".format(kindWord,dayWord,description,feels_like,funnyWord)
        print(tweet)
        api.update_status(status=tweet)
    except:
        tweet = "{}!\n{} hava {} ve sıcaklık {} derece!\n\n#HavaDurumu".format(kindWord, dayWord, description, feels_like,funnyWord)
        print(tweet)
        api.update_status(status=tweet)

def sendRainAlarm(status):
    tweet = "Dikkat! Bir saat sonra yağmur yağabilir!\n\n#Yağmur #HavaDurumu"
    print(tweet)
    api.update_status(status=tweet)