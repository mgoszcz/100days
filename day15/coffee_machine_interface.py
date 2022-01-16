from day15.coffee_machine.coffee_machine import CoffeeMachine
from day15.coffee_machine.coffee_types import COFFEE_TYPES

COFFEE_TYPES_NAMES = list(COFFEE_TYPES.keys())
coffee_machine = CoffeeMachine()


def get_user_input(message: str) -> str:
    user_input = input(message)
    if user_input == 'off':
        print('Turning off...')
        exit(0)
    elif user_input == 'report':
        print(coffee_machine.report())
    return user_input


def ask_for_coffee_type() -> str:
    coffee_typed = get_user_input(f'What would you like? {COFFEE_TYPES_NAMES}: ')
    if coffee_typed not in COFFEE_TYPES_NAMES:
        if coffee_typed != 'report':
            print('Invalid coffee name, try again.')
        coffee_typed = ask_for_coffee_type()
    return coffee_typed


while True:
    coffee_type = ask_for_coffee_type()
    resources_check = coffee_machine.check_resources(coffee_type)
    if not resources_check[0]:
        print(f'Sorry there is not enough {resources_check[1]}.')
        continue
    if not coffee_machine.coins_collector.insert_coins(coffee_type):
        continue
    if coffee_machine.make_coffee(coffee_type):
        print(f'Here is your {coffee_type}. Enjoy!')
    else:
        print('Something went wrong')
