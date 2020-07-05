import tweepy
import json

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
    tweet = "{}!\nBugün hava {} ve {} derece!".format(kindWord,status["weather"][0]["description"],status["feels_like"]["day"])
    print(tweet)
    api.update_status(status=tweet)

def sendRainAlarm(status):
    tweet = "Dikkat! Bir saat sonra yağmur yağabilir!"
    print(tweet)
    api.update_status(status=tweet)