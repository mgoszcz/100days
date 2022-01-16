"""Module contains CoffeeMachine class"""
from typing import Tuple, Optional

from day15.coffee_machine.coffee_types import COFFEE_TYPES


class _CoinsCollector:
    QUARTER = 0.25
    DIME = 0.1
    NICKLE = 0.05
    PENNY = 0.01

    @staticmethod
    def _calculate_return(total: float, cost: float) -> float:
        return round(total - cost, 2)

    @staticmethod
    def _process_input(input) -> int:
        if input == 'off':
            exit(0)
        else:
            return int(input)

    @classmethod
    def insert_coins(cls, coffee: str):
        """Method handles coins inserting"""
        quarters = cls._process_input(input("Quarters amount: "))
        dimes = cls._process_input(input("Dimes amount: "))
        nickles = cls._process_input(input("Nickles amount: "))
        pennies = cls._process_input(input("Pennies amount: "))
        total_inserted = quarters * cls.QUARTER + nickles * cls.NICKLE + dimes * cls.DIME + pennies * cls.PENNY
        coffee_cost = COFFEE_TYPES.get(coffee).get('cost')
        if total_inserted < coffee_cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        return_value = cls._calculate_return(total_inserted, coffee_cost)
        if return_value > 0:
            print(f'Here is ${return_value} dollars in change.')
        elif return_value < 0:
            raise RuntimeError('Return value cannot be negative')
        return True


class CoffeeMachine:
    """Coffee Machine class"""

    def __init__(self) -> None:
        self._water_tank = 300
        self._milk_tank = 200
        self._coffee_dispenser = 100
        self._money_collected = 0
        self.coins_collector = _CoinsCollector

    def check_resources(self, coffee: str) -> Tuple[bool, str]:
        """Check if resources are sufficient for coffee making"""
        if self._water_tank < COFFEE_TYPES.get(coffee).get('ingredients').get('water', 0):
            return False, 'water'
        if self._coffee_dispenser < COFFEE_TYPES.get(coffee).get('ingredients').get('coffee', 0):
            return False, 'coffee'
        if self._milk_tank < COFFEE_TYPES.get(coffee).get('ingredients').get('milk', 0):
            return False, 'milk'
        return True, ''

    def report(self) -> str:
        """Return report of current resources amount"""
        return f'Water: {self._water_tank}ml\nMilk: {self._milk_tank}ml\nCoffee: {self._coffee_dispenser}g\n' \
               f'Money: {self._money_collected}$'

    def make_coffee(self, coffee: str) -> bool:
        """Make coffee"""
        self._water_tank -= COFFEE_TYPES.get(coffee).get('ingredients').get('water', 0)
        self._coffee_dispenser -= COFFEE_TYPES.get(coffee).get('ingredients').get('coffee', 0)
        self._milk_tank -= COFFEE_TYPES.get(coffee).get('ingredients').get('milk', 0)
        self._money_collected += COFFEE_TYPES.get(coffee).get('cost', 0)
        return True
