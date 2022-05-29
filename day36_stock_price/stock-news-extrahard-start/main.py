import os
import smtplib

import requests

STOCK = "ROK"
COMPANY_NAME = "Rockwell Automation"

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
AV_URL = 'https://www.alphavantage.co/query'
NEWS_API_URL = 'https://newsapi.org/v2/everything'
DAILY_TIME_SERIES_DICT_KEY = 'Time Series (Daily)'
IGNORE_THRESHOLD = True
MY_EMAIL = "test.mg.python@gmail.com"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
query_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': f'{STOCK}',
    'outputsize': 'full',
    'apikey': {ALPHA_VANTAGE_API_KEY}
}
stock_response = requests.get(url=AV_URL, params=query_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
daily_data_keys = list(stock_data.get(DAILY_TIME_SERIES_DICT_KEY).keys())
previous_day_date = daily_data_keys[1]
last_day_price = float(stock_data.get(DAILY_TIME_SERIES_DICT_KEY).get(daily_data_keys[0]).get('4. close'))
previous_day_price = float(stock_data.get(DAILY_TIME_SERIES_DICT_KEY).get(daily_data_keys[1]).get('4. close'))
difference = last_day_price - previous_day_price
percentage = difference / previous_day_price * 100
if abs(percentage) < 5 and not IGNORE_THRESHOLD:
    exit(0)

## STEP 2: Use https://newsapi.org
query_params = {
    'q': COMPANY_NAME,
    'from': previous_day_date,
    'sortBy': 'popularity',
    'apiKey': NEWS_API_KEY
}
news_response = requests.get(url=NEWS_API_URL, params=query_params)
news_response.raise_for_status()
news_data = news_response.json()
articles = news_data.get('articles')

## STEP 3: Send email with price and percentage change and link to top 3 articles
message_title = f'{STOCK} price changed {percentage:.2f}%'
message = f'{STOCK} price changed by {percentage:.2f}% to {last_day_price:.2f}\n\nRelated news:\n\n'
if len(articles) == 0:
    message += 'No News found for last two trading days'
else:
    for article in articles[:3]:
        message += f'{article.get("title")}\n\n{article.get("description")}\n\n{article.get("url")}\n\n\n'

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="marcin.goszczynski88@gmail.com",
                    msg=f"Subject:{message_title}\n\n{message}")
