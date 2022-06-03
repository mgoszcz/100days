"""
1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
    International Air Transport Association (IATA) codes for each city.
    Most of the cities in the sheet include multiple airports,
    you want the city code (not the airport code see here).

2. Use the Flight Search API to check for the cheapest flights from tomorrow
    to 6 months later for all the cities in the Google Sheet.

3. If the price is lower than the lowest price listed in the Google Sheet then
    send an SMS to your own number with the Twilio API (or email).

4. The SMS (email) should include the departure airport IATA code,
    destination airport IATA code, departure city, destination city,
    flight price and flight dates. e.g.
    'Low price alert! Only $41 to fly from London-STN to Berlin-SXF,
    from 2020-08-25 to 2020-09-10'
"""
import os
import smtplib

from day39_flight_finder.destinations import Destinations
from day39_flight_finder.flight_search import FlightSearch

MESSAGE_TEMPLATE = 'LOW price alert! Only {price} PLN to fly from {city_from}-{iata_fly_from}' \
                   ' to {city_to}-{iata_fly_to}\nFrom {departure_time} to {return_time}'
TITLE_TEMPLATE = 'Low price flight to {destination} found!'
MY_EMAIL = "test.mg.python@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
destinations = Destinations()
flight_search = FlightSearch()
flight_search.departure_city = 'Frankfurt'

result = []


def send_email(flight_data):
    message = MESSAGE_TEMPLATE.format(price=flight_data.price, city_from=flight_data.city_from,
                                      iata_fly_from=flight_data.fly_from,
                                      city_to=flight_data.city_to, iata_fly_to=flight_data.fly_to,
                                      departure_time=flight_data.date_time_departure.strftime("%d-%m-%Y %H:%M:%S"),
                                      return_time=flight_data.date_time_return.strftime("%d-%m-%Y %H:%M:%S"))
    title = TITLE_TEMPLATE.format(destination=flight_data.city_to)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="marcin.goszczynski88@gmail.com",
                            msg=f"Subject:{title}\n\n{message}")


for destination in destinations.destinations:
    flight = flight_search.find_cheapest_flights(destination.iata_code)
    if not flight:
        continue
    if flight.price < destination.lowest_price:
        result.append(flight)

for flight in result:
    send_email(flight)
