sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'

# create dict with length of words in sentence
# words = sentence.replace('?', '').split()
print({word:len(word) for word in sentence.replace('?', '').split()})


weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24
}
'Convert celsius to Fahrenheit'
print({day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()})

