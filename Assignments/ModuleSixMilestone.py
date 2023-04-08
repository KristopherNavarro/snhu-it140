# Created by:   Kristopher Navarro
# GitHub:       https://github.com/KristopherNavarro/snhu-it140
# Class:        SNHU IT-140-J4175
# Instructor:   Patrick Moore
# Term:         23EW4
# Date:         8 April 2023
#
###########################################################################

# To keep gameplay clean, import os to use os.system('cls') to clear the screen
# and import the sleep module from time to make sure the screen isn't cleared too soon
import os
from time import sleep

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# A tuples of verbs associated with movement and cardinal directions.
# User input is compared to both of these lists for validation
# User is able to more naturally input directions
movement_verbs = ('Go', 'Move', 'Head', 'Travel', 'Step', 'Trek', 'Advance', 'Proceed', 'Run', 'Walk', 'Crawl')
heading = ('North', 'South', 'East', 'West')

# The current room variable. This updates with each valid move.
current_room = 'Great Hall'

print('''
   ---   Welcome to the Mansion!   ---
Navigate around the rooms at your leisure!
''')

# Begin while loop for user interaction
while True:
    os.system('cls')    # This will keep the screen clean
    print(f'\nYou are in the {current_room}. \n')   # Prints current room status

    # Take user input as a titlecase string then split into tokens for validation
    user_input = str(input('What would you like to do? \n')).title()
    tokens = user_input.split()

    # The following valid_tokens list is important for validating correct statements are given by user.
    # Any valid tokens are appended to this during the next for loop, then accessed after the loop
    # completes to validate whether the user supplied a valid input.
    valid_tokens = []

    # Begin for loop to parse and validate commands given by user
    for token in tokens:
        if token in movement_verbs: # This validates movement commands
            valid_tokens.append(token)  # Appends valid movement_verb to valid_tokens

            # Begin for loop to parse and validate heading
            for token in tokens:
                if token in heading:     #This validates heading
                    valid_tokens.append(token)  # Appends valid heading to valid_tokens

                    # Invalid cardinal directions will raise a KeyError
                    # Try block to handle any KeyErrors
                    try:
                        current_room = rooms[current_room][token]
                        print(f'\nYou are now in the {current_room}. \n')
                        sleep(2)    # waits before returning to the while loop which will clear screen
                    except KeyError:
                        print('\nOnly ghosts can walk through walls, try again. \n')
                        sleep(2)    # waits before returning to while loop

    # After parsing for movements, check if the user wishes to exit and break while loop if true
    if 'Exit' in tokens:
        break

    # Check that the user has input a valid command.
    # If valid_tokens contains zero elements then the user has input an invalid command.
    # print out a notification letting the user know, then wait before returning to the while loop
    elif len(valid_tokens) == 0:
        print('\nNot a valid command, try again. \n')
        sleep(2)

# If while loop is broken, clear screen and print some gratitude.
os.system('cls')
print('\n  Thanks for playing! \n \n')