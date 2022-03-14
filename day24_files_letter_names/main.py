#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os
print(os.getcwd())
NAMES_FILE = 'Input/Names/invited_names.txt'
SAMPLE_MAIL = 'Input/Letters/starting_letter.txt'
OUTPUT_DIRECTORY = 'Output/ReadyToSend'
FILE_NAME_TEMPLATE = 'letter_for_{}.txt'
STRING_TO_REPLACE = '[name]'
with open(SAMPLE_MAIL, 'r') as file_handle:
    SAMPLE_MAIL_TEXT = file_handle.read()

with open(NAMES_FILE, 'r') as file_handle:
    names = file_handle.read().split()

for name in names:
    file_path = os.path.join(OUTPUT_DIRECTORY, FILE_NAME_TEMPLATE.format(name))
    text_to_save = SAMPLE_MAIL_TEXT.replace(STRING_TO_REPLACE, name)
    with open(file_path, 'w') as file_handle:
        file_handle.write(text_to_save)
