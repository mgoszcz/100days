import smtplib

import requests


# LAT = 50.2584
# LON = 19.0275
import os

API_KEY = os.environ.get('OWM_API_KEY')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

LAT = 52.220852
LON = 6.890950
MY_EMAIL = "test.mg.python@gmail.com"

parameters = {
    'lat': LAT,
    'lon': LON,
    'units': 'metric',
    'appid': API_KEY
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
data = response.json()

rain_today = False
for hour in data.get('hourly')[:12]:
    for item in hour.get('weather'):
        if item.get('id') < 700:
            rain_today = True



if rain_today:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="marcin.goszczynski88@gmail.com",
                        msg="Subject:It will rain today\n\nTake an umbrella")


pass
