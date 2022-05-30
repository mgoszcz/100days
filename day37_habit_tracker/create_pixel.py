from datetime import datetime

import requests

from day37_habit_tracker.my_token import TOKEN

today = datetime.now()

USERNAME = 'mgoszcz'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
graphs_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
steps_graph_endpoint = f'{graphs_endpoint}/steps1'

quantity = input('Provide today\'s steps quantity: ')

headers = {'X-USER-TOKEN': TOKEN}
pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': str(quantity),
}
response = requests.post(url=steps_graph_endpoint, json=pixel_config, headers=headers)
print(response.text)
