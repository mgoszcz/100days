import requests
from datetime import datetime

from day37_habit_tracker.my_token import TOKEN

USERNAME = 'mgoszcz'
pixela_endpoint = 'https://pixe.la/v1/users'

### Create user
# user_params = {
#     'token': TOKEN,
#     'username': 'mgoszcz',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

### Create Graph
graphs_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# graph_config = {
#     'id': 'steps1',
#     'name': 'Steps Graph',
#     'unit': 'steps',
#     'type': 'int',
#     'color': 'sora'
# }
#
# headers = {'X-USER-TOKEN': TOKEN}
#
# response = requests.post(url=graphs_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2022, month=5, day=29)

### Create pixel
steps_graph_endpoint = f'{graphs_endpoint}/steps1'
headers = {'X-USER-TOKEN': TOKEN}
# pixel_config = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '35',
# }
#
# response = requests.post(url=steps_graph_endpoint, json=pixel_config, headers=headers)
# print(response.text)

### MOdify PIxel
# endpoint = f'{steps_graph_endpoint}/{today.strftime("%Y%m%d")}'
# params = {'quantity': '100'}
#
# response = requests.put(url=endpoint, json=params, headers=headers)
# print(response.text)

today = datetime.now()

### Delete pixel
endpoint = f'{steps_graph_endpoint}/{today.strftime("%Y%m%d")}'
response = requests.delete(url=endpoint, headers=headers)
print(response.text)
