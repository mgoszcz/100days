from datetime import datetime

import requests

from day38_google_spreadsheet.api_keys import APP_ID, APP_KEY, SHEETY_BEARER

ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/8e153edaafa3b1508523a323fc78533d/myWorkouts/workouts'

query = input('Excercise: ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

params = {
    'query': query,
    'gender': 'male',
    'weight_kg': 95,
    'height_cm': 198,
    'age': 34
}

response = requests.post(url=ENDPOINT, headers=headers, json=params)
response.raise_for_status()
exercise_data = response.json().get('exercises')

current_datetime = datetime.now()
date = current_datetime.strftime('%d/%m/%Y')
time = current_datetime.strftime('%H:%M:%S')
sheety_headers = {'Authorization': f'Bearer {SHEETY_BEARER}'}

for exercise in exercise_data:
    sheety_params = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise.get('name'),
            'duration': exercise.get('duration_min'),
            'calories': exercise.get('nf_calories'),
        }
    }
    resp = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=sheety_params)
    print(resp.text)
