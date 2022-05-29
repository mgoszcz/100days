"""
If the ISS is close to my current position (+/- 5 degrees)
and it is currently dark
Then send me an email to tell me to look up
run the code every 60 seconds
"""
import os
import smtplib
import time
from datetime import datetime
from typing import Tuple

import pytz
import requests

MY_LAT = 50.223434
MY_LONG = 18.995586
UTC = pytz.UTC
ISS_CLOSE = False
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def get_iss_position() -> Tuple[float]:
    """
    Get current position of ISS
    :return: (latitude, longitude)
    """
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    lat = float(response.json().get('iss_position').get('latitude'))
    long = float(response.json().get('iss_position').get('longitude'))
    return lat, long


def get_sunrise_sunset_time() -> Tuple[datetime]:
    """
    Get sunrise and sunset time
    :return: (sunrise, sunset)
    """
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }

    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    sunset = datetime.fromisoformat(response.json().get('results').get('sunset'))
    sunrise = datetime.fromisoformat(response.json().get('results').get('sunrise'))
    return sunrise, sunset


def is_it_night(sunrise: datetime, sunset: datetime, current: datetime) -> bool:
    """Check whether it is night"""
    if current <= sunrise or current >= sunset:
        return True
    return False


def is_iss_close(position: Tuple[float]) -> bool:
    """Check if IIS is close to current location (+/- 5 degrees)"""
    if not position[0] >= MY_LAT - 5 and position[0] <= MY_LAT + 5:
        return False
    if not position[1] >= MY_LONG - 5 and position[1] <= MY_LONG + 5:
        return False
    return True


def send_mail(close: bool) -> None:
    """
    Send email if it is night and IIS is close
    :param close: boolean
    :return: None
    """
    global ISS_CLOSE
    if not close:
        if ISS_CLOSE:
            ISS_CLOSE = False
        print('ISS too far')
        return
    if close:
        if ISS_CLOSE:
            print('ISS close, mail already sent')
            return
        ISS_CLOSE = True
        print('ISS close, send mail')
    my_email = "test.mg.python@gmail.com"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=my_email, to_addrs="marcin.goszczynski88@gmail.com",
                            msg="Subject:ISS Close\n\nLook Up!")


def sleeper(sunrise: datetime, sunset: datetime) -> None:
    """Sleep specific amount of time (determine dynamically depending on time and ISS distance)"""
    cur_time = datetime.utcnow().replace(tzinfo=UTC)
    sleeping_time = 60
    if sunrise <= cur_time <= sunset:
        delta = sunset - cur_time
        if delta.seconds > 3600:
            sleeping_time = 3600
        elif delta.seconds > 1800:
            sleeping_time = 1800
        elif delta.seconds > 900:
            sleeping_time = 900
        else:
            sleeping_time = 300

    print(f'Sleeping {sleeping_time} seconds')
    time.sleep(sleeping_time)


while True:
    print('Checking')
    iss_position = get_iss_position()
    sunrise_sunset = get_sunrise_sunset_time()
    current_time = datetime.utcnow().replace(tzinfo=UTC)
    if is_it_night(sunrise_sunset[0], sunrise_sunset[1], current_time):
        send_mail(is_iss_close(iss_position))
    sleeper(sunrise_sunset[0], sunrise_sunset[1])
