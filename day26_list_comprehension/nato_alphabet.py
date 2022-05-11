
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {}
for (index, row) in data.iterrows():
    alphabet_dict[row.letter.lower()] = row.code

word = input('Type word: ')
print([alphabet_dict[letter.lower()] for letter in word])

pass