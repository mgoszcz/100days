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
from day39_flight_finder.destinations import Destinations
from day39_flight_finder.flight_search import FlightSearch

destinations = Destinations()
flight_search = FlightSearch()
flight_search.departure_city = 'Katowice'

result = []

for destination in destinations.destinations:
    flight = flight_search.find_cheapest_flights(destination.iata_code)
    if not flight:
        continue
    if flight.price < destination.lowest_price:
        result.append(flight)

for flight in result:
    print(f'LOW price alert! Only {flight.price} EUR to fly from {flight.city_from}-{flight.fly_from}'
          f' to {flight.city_to}-{flight.fly_to}\nDate: {flight.date_time.strftime("%d-%m-%Y %H:%M:%S")}')
