

with open('weather_data.csv', 'r') as file_handler:
    data = file_handler.readlines()

import csv

with open('weather_data.csv', 'r') as file_handler:
    csv_data = csv.reader(file_handler)
    temperatures = []
    for row in csv_data:
        print(row)
        if csv_data.line_num > 1:
            temperatures.append(int(row[1]))

print(temperatures)

import pandas

pandas_data = pandas.read_csv('weather_data.csv')
print(pandas_data)
temperatures = pandas_data.temp
print(f'Average tempareture: {sum(temperatures)/len(temperatures)} or: {temperatures.mean()}')
print(f'Max temperature: {temperatures.get(temperatures.argmax())} or: {temperatures.max()}')

# Get data in row
print(pandas_data[pandas_data.day == 'Monday'])
# Get highest temp
print(pandas_data[pandas_data.temp == pandas_data.temp.max()])

monday = pandas_data[pandas_data.day == 'Monday']
print(monday.temp)
print((monday.temp * 1.8) + 32)

# Create a dataframe
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
my_data = pandas.DataFrame(data_dict)
my_data.to_csv('my_file.csv')
pass