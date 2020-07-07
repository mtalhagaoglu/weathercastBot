import requests
import json
with open("secret.json") as json_data_file:
    data = json.load(json_data_file)

#These settings for istanbul,tr

lat = 41.01384
lon = 28.949659
appid = data["openWeatherApiKey"]
lang = "tr"
units = "metric"

url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&lang={}&units={}".format(lat,lon,appid,lang,units)

def makeRequest():
    data = requests.get(url)
    json = data.json()
    return json

def getCurrent():
    data = makeRequest()
    current = data["current"]
    return current

def getToday():
    data = makeRequest()
    today = data["daily"][0]
    return today

def getTomorrow():
    data = makeRequest()
    tomorrow = data["daily"][1]
    return tomorrow

def rainyCheck():
    data = makeRequest()
    current = data["hourly"][0]
    nextHour = data["hourly"][1]
    if current["weather"][0]["id"] != nextHour["weather"][0]["id"] and ( 199 < nextHour["weather"][0]["id"] < 600):
        return nextHour
    else:
        return False
