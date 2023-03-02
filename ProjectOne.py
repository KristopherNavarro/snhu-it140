############################################################
#                                                          #
#  Create a small program that asks for the user's name    #
#  and age and calculates their birth year.                #
#                                                          #
############################################################

# In this program, I will want to use as little user input
# as possible. This will require retrieving the current year
# from the 'datetime' package.

# Import the 'datetime' package

from datetime import datetime

# Create a 'while loop' that allows the program to restart if desired
# create a variable named 'repeat' set to 'y'
# at the end of the first pass of the loop, user will be prompted for y/n,
# this will reset the 'repeat' variable and break the loop if 'n'

repeat = 'y'
name = input('What is your name? ')

while (repeat == 'y'):

    # Add a 'try' block to handle if user enters non-numeric characters
    # then add an 'except' block to handle any 'valueErrors' by printing
    # instructions for what is expected and restarting the loop
    try:
        age = int(input('What is your age? '))
    except ValueError:
        print('please enter a numerical age...')
        continue

    # Retrieve the current year from 'datetime' and assign to 'current_year'
    # then perform the calculation to find birth year, assign to 'year_born'
    current_year = int(datetime.now().year)
    year_born = current_year - age

    # Have a little fun: if a user enters an age that results in a birth year
    # less than 0, convert using abs() and print as a BC year.
    if year_born >= 0:
        print(f'''
Hello, {name}! You were born in {year_born}.
            ''')
    else:
        print(f'''
Hello, {name}! You were born in {abs(year_born)} BC! Whoa! Are you a Time Lord?.
        ''')

    # Request user input asking 'Run again? y/n', assign to 'repeat' variable
    # 'y' will continue the loop, 'n' will break the loop, ending the program
    repeat = input('Run again? y/n ')

