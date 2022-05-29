import datetime
import os
import smtplib
from random import randint

EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

if datetime.datetime.now().weekday() != 0:
    exit(0)

with open('quotes.txt') as file_handler:
    quotes = file_handler.readlines()

quote_number = randint(0, len(quotes))
quote = quotes[quote_number]

my_email = "test.mg.python@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=my_email, password=EMAIL_PASSWORD)
    connection.sendmail(from_addr=my_email, to_addrs="marcin.goszczynski88@gmail.com",
                        msg=f"Subject:Monday Quote\n\n{quote}")
