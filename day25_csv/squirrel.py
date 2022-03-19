import pandas

DATA_FILE = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'


data = pandas.read_csv(DATA_FILE)
fur_colors = data.get('Primary Fur Color')
fur_colors.value_counts().to_csv('fur_colors.csv', header=['Count'], index_label='Fur Color')
