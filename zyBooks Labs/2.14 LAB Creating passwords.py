# This LAB has 3 parts:
#
# (1) Prompt the user to enter two words and a number, storing each into separate variables.
# Then, output those three values on a single line separated by a space. (Submit for 1 point)
#
# Ex:   If the input is:    yellow
#                           Daisy
#                           6
#       the output after
#       the prompts is:    'You entered: yellow Daisy 6'
#                           Note: User input is not part of the program output.

# Delete the input prompt string before submitting
input1 = input('Enter a word: ')
input2 = input('Enter a second word: ')
input3 = input('Enter a number: ')

concat_inputs = f'{input1} {input2} {input3}'
print(f'You entered: {concat_inputs}\n')



# (2) Output two passwords using a combination of the user input. Format the passwords as shown below.
# (Submit for 2 points, so 3 points total).
#
# Ex:   If the input is:    yellow
#                           Daisy
#                           6
#       the output after
#       the prompts is:  '''You entered: yellow Daisy 6
#
#                           First password: yellow_Daisy
#                           Second password: 6yellow6'''

password1 = f'{input1}_{input2}'
password2 = f'{input3}{input1}{input3}'

print(f'''You entered: {concat_inputs}

First password: {password1}
Second password: {password2}''')





# (3) Output the length of each password (the number of characters in the strings).
# (Submit for 2 points, so 5 points total).
#
# Ex:   If the input is:    yellow
#                           Daisy
#                           6
#       the output after
#       the prompts is:  '''You entered: yellow Daisy 6
#
#                           First password: yellow_Daisy
#                           Second password: 6yellow6
#
#                           Number of characters in yellow_Daisy: 12
#                           Number of characters in 6yellow6: 8'''


length_p2 = len(password1)
length_p3 = len(password2)

print(f'''You entered: {concat_inputs}

First password: {password1}
Second password: {password2}

Number of characters in {password1}: {length_p2}
Number of characters in {password2}: {length_p3}''')
