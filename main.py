from openApi import *
from twitter import *
from datetime import datetime
from time import *
import pytz

controlTimes = ["07","18","22"]

while True:
    tz = pytz.timezone('Europe/Istanbul')  #Timezone
    hour = datetime.now(tz).strftime("%H")
    minute = datetime.now(tz).strftime("%M")
    print(datetime.now(tz))
    #if hour in controlTimes:
    if hour in controlTimes and minute == "00":
        if hour == "22":
            sendDailyTweet(getTomorrow(),hour)
        else:
            sendDailyTweet(getToday(),hour)
        # Tweet today's weathercast

    rainStatus = rainyCheck()
    if rainStatus:
        sendRainAlarm(rainStatus)
        print("Rain alarm")
        # Tweet rain status

    minute = int(minute)
    if minute >= 30:
        wait = 60 - minute
    else:
        wait = 30 - minute
    print("Wake me {} min later sweetie ♥".format(wait))
    sleep(60 * wait) #30 minutes