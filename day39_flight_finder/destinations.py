"""Handle destinations sheet"""
from typing import List, Dict

import requests

from day39_flight_finder.flight_search import FlightSearch
from day39_flight_finder.tokens import SHEETY_BEARER

SHEETY_ENDPOINT = 'https://api.sheety.co/8e153edaafa3b1508523a323fc78533d/flightDeals/prices'
SHEETY_HEADERS = {'Authorization': f'Bearer {SHEETY_BEARER}'}


class _Destination:
    def __init__(self, destination_dict: Dict) -> None:
        self.city = destination_dict.get('city')
        self.iata_code = destination_dict.get('iataCode')
        self.lowest_price = destination_dict.get('lowestPrice')


class Destinations:
    def __init__(self) -> None:
        self._destinations = []
        self._populate_iata_codes()

    @staticmethod
    def _get_destinations() -> List[Dict]:
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        response.raise_for_status()
        return response.json().get('prices')

    @property
    def destinations(self) -> List[_Destination]:
        if not self._destinations:
            for destination in self._get_destinations():
                self._destinations.append(_Destination(destination))
        return self._destinations

    def _populate_iata_codes(self):
        for destination in self._get_destinations():
            if not destination.get('iataCode'):
                parameters = {'price': {'iataCode': FlightSearch.get_city_iata_code(destination.get('city'))}}
                response = requests.put(url=f'{SHEETY_ENDPOINT}/{destination.get("id")}', headers=SHEETY_HEADERS,
                                        json=parameters)
                print(response.text)

Destinations()
