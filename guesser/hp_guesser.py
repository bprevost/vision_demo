#!/usr/bin/python3

import json

# Name of the data file
DATAFILE = 'hp_guesser.json'

# Open the data file
file_pointer = open(DATAFILE, 'r')
data = json.load(file_pointer)

# Ask the questions
question = 'Is it magical?' # Starting question
while True:
    response = input(question + ' (yes/no) ')
    if isinstance(data[question], dict):
        prior_question = question
        prior_response = response
        result = data[question][response]
        question = result
    elif response == 'yes':
        print('I got it!')
        break
    elif response == 'no':
        print('You stumped me!')
        answer = input('OK, who is it then? ')
        new_question = input('Give me a "yes" question that would help identify ' + answer + '.\n')
        if new_question[-1] == '.':
            new_question = new_question[:-1] + '?'
        elif new_question[-1] != '?':
            new_question = new_question + '?'

        answer = 'Is it ' + answer + '?'
        data[answer] = 0
        data[new_question] = {'yes': answer, 'no': question}
        data[prior_question][prior_response] = new_question
        print('Thanks!')
        break

# Close the data file
file_pointer.close()

# Save the data to a file
with open(DATAFILE, 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)
