# Weathercast Bot

A twitter weathercastbot. It's live on => https://twitter.com/havadurumubot

  - Everyday at 7 am it sends daily weathercast
  - Everyday at 6 pm it sends this night's weathercast
  - Everyday at 11 pm it sends tomorrow's weathercast
  - Every 30 minutes it checks rain status and if there is it sends tweet
  - with %20 chance it will send tweets with selected funny word from templastes (you can customize them for your language)
 
### Tech
* Python

### Installation

I am suggesting you to create a virtual environmet.
This link can help you => https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04

You have to get your twitter and openweather api key.
Create a secret.json inside of weathercastBot folder. It have to looks like this:

```sh
{
  "openWeatherApiKey": "",
  "tw_consumer_key": "",
  "tw_consumer_secret": "",
  "tw_access_token": "",
  "tw_access_token_secret": ""
}
```

You can customize your city with editing openApi.py. https://openweathermap.org/api
After create secret.json, you can run .py file.

```sh
$ cd weathercastBot
$ pip install -r requirements.txt
$ python3 main.py
```

### ToDo

- Use cron instead of sleep (done)
