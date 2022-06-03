import requests
from datetime import datetime, timedelta

from day39_flight_finder.tokens import TEQUILLA_API_KEY

TEQUILLA_SERVER = 'https://tequila-api.kiwi.com'
LOCATION_SEARCH_ENDPOINT = f'{TEQUILLA_SERVER}/locations/query'
FLIGHT_SEARCH_ENDPOINT = f'{TEQUILLA_SERVER}/search'
HEADER = {'apikey': TEQUILLA_API_KEY}

class _Flight:
    def __init__(self, flight_dict):
        self.price = flight_dict.get('price')
        self.city_from = flight_dict.get('cityFrom')
        self.city_to = flight_dict.get('cityTo')
        self.fly_from = flight_dict.get('flyFrom')
        self.fly_to = flight_dict.get('flyTo')
        self.date_time_departure = datetime.fromtimestamp(flight_dict.get('route')[0].get('dTime'))
        self.date_time_return = datetime.fromtimestamp(flight_dict.get('route')[1].get('dTime'))


class FlightSearch:

    def __init__(self) -> None:
        self._departure_city = None
        self._departure_iata_code = None

    @staticmethod
    def get_city_iata_code(city_name: str) -> str:
        parameters = {
            'term': city_name,
            'location_types': 'city'
        }
        response = requests.get(url=LOCATION_SEARCH_ENDPOINT, params=parameters, headers=HEADER)
        response.raise_for_status()
        return response.json().get('locations')[0].get('code')

    @property
    def departure_city(self):
        return self._departure_city

    @departure_city.setter
    def departure_city(self, value: str):
        iata_code = self.get_city_iata_code(value)
        if not iata_code:
            raise AttributeError('City does not have IATA code, provide another city with airports')
        self._departure_city = value
        self._departure_iata_code = iata_code

    def find_cheapest_flights(self, destination) -> _Flight:
        if not self._departure_city:
            raise RuntimeError('Set up departure city in Flight search\ne.g. FlightSearch().departure_city = Paris')
        tomorrow = datetime.now() + timedelta(days=1)
        six_months_later = tomorrow + timedelta(days=30 * 6)
        parameters = {
            'fly_from': self._departure_iata_code,
            'fly_to': destination,
            'date_from': tomorrow.strftime('%d/%m/%Y'),
            'date_to': six_months_later.strftime('%d/%m/%Y'),
            'sort': 'price',
            'max_stopovers': 0,
            'flight_type': 'round',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 14,
            'curr': 'PLN'
        }
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=HEADER, params=parameters)
        response.raise_for_status()
        flights = response.json().get('data')
        return _Flight(flights[0]) if flights else None
