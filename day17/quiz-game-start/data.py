import requests

def collect_data():
    amount = input("Type amount of questions (default is 10): ")
    if amount == '':
        amount = 10
    difficulty = input("Select difficulty level (easy/medium/hard/any): ")
    if difficulty not in ('easy', 'medium', 'hard', 'any'):
        print('Incorrect difficulty, Exiting...')
        exit(1)
    if difficulty == 'any':
        url = f'https://opentdb.com/api.php?amount={amount}&type=boolean'
    else:
        url = f'https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=boolean'
    req = requests.get(url).json()
    return req.get('results')


question_data = collect_data()
