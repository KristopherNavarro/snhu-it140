# Room layout for Text Based Game

import os
from time import sleep
import random as random
from random import uniform

health = 2      # Starting health, chances to face the Boss
pages = 0       # increments with ever book page collected
current_room = 'Entry'
breadcrumbs = []
moves = 0
inventory = {
    'Slot 1': '',
    'Slot 2': '',
    'Slot 3': ''}

class Typewriter:
    ''' Iterates over a string and prints with a varying pause between each character to mimmick a typewriter.

    All methods append a UTC timestamp to a global list named 'variability' at the beginning of each iteration.

    --slow(self, stop=''):
        takes
        prints at a slow speed

    -- med():
        prints at a medium speed

    -- fast():
        prints at a fast speed

    '''
    def slow(self,stop=''):
        global variability
        for ch in self[:-1]:
            print(ch, end='', flush=True)
            sleep(uniform(0.1,0.25))
        print(self[-1], end=stop, flush=True)

    def med(self,stop=''):
        for ch in self[:-1]:
            print(ch, end='', flush=True)
            sleep(uniform(0.005,0.1))
        print(self[-1], end=stop, flush=True)

    def fast(self,stop=''):
        for ch in self[:-1]:
            print(ch, end='', flush=True)
            sleep(uniform(0.001,0.01))
        print(self[-1], end=stop, flush=True)

def introduction():
    os.system('cls')
    print(r'''
  <@)>^-^-    Welcome to Marrowood Mansion!    -^-^-<(@>
    
                        ͜^͜^͜^͜ 
           !͜͜!͜͜!͜͜!͜͜/ _    _\͜͜!͜͜!͜͜!͜͜! 
          /͜͜/͜͜/͜͜/͜͜/  <( )>  \͜͜\͜͜\͜͜\͜͜\    
         /͜͜/͜͜/͜͜/͜͜/  _    _  _\͜͜\͜͜\͜͜\͜͜\   
          │  _   _   _ _  _  __   _   _ _   │  
          │ _   ┌┬┐ _    _┌┬┐  _   _┌┬┐ _  _│  
          │    _├┼┤  _    ├┼┤ _     ├┼┤   _ │
          │_  _ └┴┘_    _ └┴┘   _   └┴┘ _   │
          │    _    _ ͜͜͜͜͜͜͜͜͜͜͜ _   _ _   │            
          │ _   _    /͜͜/͜͜|͜͜\͜͜\ _     _  │
          │_    ┌┬┐ _ || ┌───┐_||  _┌┬┐    _│  
          │  _ _├┼┤   ||_│ ▒ │ ||   ├┼┤ _   │
          │ _   └┴┘  _|| │   │ ||-  └┴┘  _  │
   ~~^~~^~~^~~~~~~^~~~~~^~~~~~^~^~~~~~^~~~^^~~~~~^~~~~
                       /- - - -\
                      /- - - - -\       ''')
    sleep(1.5)
    print('''
                     Press ENTER...''',end='')
    input()

    os.system('cls')
    print(rf'''
  <@)>^-^-    Welcome to Marrowood Mansion!    -^-^-<(@>
__________________________________________________________

''')
    Typewriter.fast('''
      Something wicked was conjured in Marrowood... 


      A lively and bright dinner party, hosted by the 
  new owners of the Marrowood Estate, has taken a sinister 
  turn when curiosities became insatiable... 


''')
    sleep(1.5)
    print('''                Press ENTER to continue..''',end='')
    input()

    os.system('cls')
    print(r'''
  <@)>^-^-    Welcome to Marrowood Mansion!    -^-^-<(@>
__________________________________________________________
''')
    Typewriter.fast('''      While exploring the residence, a long-rumored 
   Altar Room was discovered, along with an ancient
   book: 

  <@)>--^~-   The Grimoire of Pope Honorius   -^-`^-<(@>  
    
      Ignorant of the power the spells within possessed, 
  the party has unleashed a demonic being upon our world. 
  Weak from materialization, the demon has retreated to 
  the Altar room after chasing the party guests from the 
  house. In the mayhem to escape the demon... 

  <@)>-^-^--~--   SIX PAGES WERE LOST    -^-~-^-`^-<(@>
  ''')
    sleep(1.5)
    print('''
                Press ENTER to continue...''',end='')
    input()

    os.system('cls')
    print(r'''
  <@)>^-^-    Welcome to Marrowood Mansion!    -^-^-<(@>
__________________________________________________________
''')
    Typewriter.fast('''    It is your quest to find the missing pages strewn
  throughout the mansion before making your way to the 
  Altar Room to vanquish the demon lurking within.

      You begin your quest in the Entry of Marrowood, 
  armed only with your wit, a bag, and the incomplete 
  Grimoire of Pope Honorius... 


                             -~^-~-^-`^-<(@
''')
    sleep(1.5)
    print('''
                Press ENTER to begin...''',end='')
    input()


def secrets(item):
    secrets_map = {
        'Servant Quarters': 'Hidden Room',
        'Office': 'Secret Passage'}
    for v in inventory.values():
        if v == item:
            return secrets_map[current_room]
        elif len(breadcrumbs) > 0:
            return breadcrumbs[-1]

def all_pages():
    if pages == 6:
        print('    You must find all of the pages first.')
        sleep(1.5)
        return 'Altar'
    else:
        print('    You have the pages, cast this demon away!')
        sleep(1.5)
        return 'Attic'
def observed():
    if location_items[current_room]['observed'] == True:
        return location_items[current_room]['item']
    else:
        print()

def room_observation():
    try:
        return room_views[current_room]
    except KeyError:
        return ''

def centered(*args, spaces):
    ''' Concatenates multiple arguments and centers based on the supplied totoal space width as spaces'''
    arg_list = []
    for arg in args:
        arg_list.append(str(arg))
    text = ''.join(arg_list)
    return text.center(spaces)








bad_moves = [
    'Only ghosts can walk through walls, try again.',
    'Your vision may be sharp, but not your sight, try again.',
    'Too much of that and we\'ll all be lost, try again.',
    'Something is amiss, try again.',
    'You won\'t vanquish much in that direction, try again.'
]

map = {
    # First Floor

    'Entry': {
        'North': 'Grand Hall',},
    'Lounge': {
        'North': 'Dining Room',
        'East': 'Grand Hall'},
    'Grand Hall': {
        'Ascend': '2nd Floor Landing',
        'Climb': '2nd Floor Landing',
        'Up': '2nd Floor Landing',
        'South': 'Entry',
        'East': 'Library',
        'West': 'Lounge'},
    'Library': {
        'North': 'Servant Hall',
        'East': 'Office',
        'West': 'Grand Hall'},
    'Office': {
        'West': 'Library'},
    'Dining Room': {
        'North': 'Sun Room',
        'South': 'Lounge',
        'East': 'Kitchen'},
    'Kitchen': {
        'North': 'Garden',
        'East': 'Pantry',
        'West': 'Dining Room'},
    'Pantry': {
        'East': 'Servant Hall',
        'West': 'Kitchen'},
    'Servant Hall': {
        'North': 'Servant Quarters',
        'South': 'Library',
        'Up': 'Master Hall',
        'Ascend': 'Master Hall',
        'Climb': 'Master Hall',
        'West': 'Pantry'},
    'Sun Room': {
        'South': 'Dining Room',
        'East': 'Garden'},
    'Garden': {
        'North': 'Hedge Maze',
        'South': 'Kitchen',
        'East': 'Servant Quarters',
        'West': 'Sun Room'},
    'Servant Quarters': {
        'South': 'Servant Hall',
        'West': 'Garden',
        'East': secrets('Key')},
    'Hedge Maze': {
        'North': 'Graveyard',
        'South': 'Garden'},
    'Graveyard': {
        'South': 'Hedge Maze'},
    'Hidden Room':{
        'West': 'Servant Quarters'},

    #Second Floor

    'Game Room': {
        'East': '2nd Floor Landing'},
    '2nd Floor Landing': {
        'North': 'Den',
        'East': 'Master Hall',
        'West': 'Game Room',
        'Down': 'Grand Hall',
        'Descend': 'Grand Hall'},
    'Master Hall': {
        'North': 'Master Suite',
        'South': 'Guest Room',
        'West': '2nd Floor Landing',
        'Up': 'Attic',
        'Ascend': 'Attic',
        'Climb': 'Attic',
        'Down': 'Servant Hall',
        'Descend': 'Servant Hall'},
    'Guest Room': {
        'North': 'Master Hall'},
    'Den': {
        'South': '2nd Floor Landing'},
    'Master Suite': {
        'South': 'Master Hall'},

    # Third floor

    'Attic': {
        'South': all_pages(),
        'Down': 'Master Hall',
        'Descend': 'Master Hall'},
    'Altar': {
        'North': 'Attic'}
}

location_items = {
    'Servant Quarters': {
        'present': True,
        'item': 'Page 1',
        'page': True,
        'observed': False},
    'Den': {
        'present': True,
        'item': 'Page 2',
        'page': True,
        'observed': False},
    'Graveyard': {
        'present': True,
        'item': 'Page 3',
        'page': True,
        'observed': False},
    'Kitchen': {
        'present': True,
        'item': 'Page 4',
        'page': True,
        'observed': False},
    'Office': {
        'present': True,
        'item': 'Page 5',
        'page': True,
        'observed': False},
    'Guest Room': {
        'present': True,
        'item': 'Page 6',
        'page': True,
        'observed': False},
}

room_views = {
    'Entry': '''    You begin your quest in the Entry of Marrowood, 
  armed only with your wit and the incomplete spellbook.''',
    'Grand Hall': '''    The Grand Hall is dimly lit from the outside 
  ambient light. Before you is a Grand Staircase.''',
    'Lounge': '',
    'Library': '',
    'Office': '',
    'Dining Room': '',
    'Kitchen': '',
    'Pantry': '',
    'Servant Hall': '',
    'Stairwell': '',
    'Sun Room': '',
    'Garden': '',
    'Servant Quarters': '',
    'Hidden Room': '',
    'Hedge Maze': '',
    'Graveyard': '',

    # 2nd floor

    'Game Room': '',
    'Den': '',
    '2nd Floor Landing': '',
    'Master Hall': '',
    'Guest Room': '',
    'Master Suite': '',
    'Stairwell': '',
    'Master Suite': '',

    # 3rd Floor

    'Attic': '',
    'Stairwell': '',
    'Alter': '',
    'Attic': '',
    'Hatch': ''}


# A tuples of verbs associated with movement and cardinal directions.
# User input is compared to both of these lists for validation
# User is able to more naturally input directions
movement_verbs = ('Go', 'Move', 'Head', 'Travel', 'Step', 'Trek', 'Advance', 'Proceed', 'Run', 'Walk', 'Crawl', 'Climb', 'Descend', 'Ascend')
heading = ('North', 'South', 'East', 'West', 'Up', 'Down', 'Climb', 'Descend', 'Ascend', 'Stairs', 'Staircase')
action_verbs = ('Get', 'Take', 'Grab')
obs_verbs = ('Look', 'See', 'Examine')


# introduction()

def display_header():
    os.system('cls')  # This will keep the screen clean
    var = 'You are in the '

    print(f'''
  @)>^-~-`- {centered(var, current_room, spaces=33)} -~^-`^-<(@
__________________________________________________________
    Moves [ {centered(moves, spaces=3)}]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
----------------------------------------------------------

   {room_observation()}


    ''', flush=True)






# Begin while loop for user interaction
while True:

    display_header()

    # Take user input as a titlecase string then split into tokens for validation
    tokens = str(input('What would you like to do? ')).title().split()

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
                        map[current_room][token]
                        breadcrumbs.append(current_room)
                        moves += 1
                        current_room = map[current_room][token]

                    except KeyError:
                        print(f'\n{random.choice(bad_moves)} \n')
                        sleep(1.5)    # waits before returning to while loop
        elif token in obs_verbs:
            valid_tokens.append(token)
            try:
                if location_items[current_room]['present'] == False:
                    print('  There is nothing to see here.')
                    sleep(1.5)
                else:
                    location_items[current_room]['observed'] = True
                    print(f'  You found a page!')
                    sleep(1.5)
            except KeyError:
                print('  There is nothing here')
                sleep(1.5)
            continue
        elif token in action_verbs:
            valid_tokens.append(token)
            try:
                if location_items[current_room]['observed'] == False:
                    print('  There is nothing to take, try looking around.')
                    sleep(1.5)
                    continue
                else:
                    # new_inventory = location_items[current_room]['item']
                    # for k,v in inventory.items():
                    #     if v == False:
                    #         inventory[k] = location_items[current_room]['item']
                    #         location_items[current_room]['item'] = False

                    if location_items[current_room]['page'] == True:
                        pages += 1
                        location_items[current_room]['page'] == False

                    # for k, v in inventory.items():
                    #     if v == False:
                    #         inventory[k] = location_items[current_room]['item']
                    #         location_items[current_room]['item'] = False
                    print(f'  You now have {location_items[current_room]["item"]}.')
                    sleep(1.5)
            except KeyError:
                print('  There is nothing to here.')
                sleep(1.5)
            continue

        elif token == 'Inventory':
            valid_tokens.append(token)
            for k,v in inventory.items():
                if v != False:
                    print(f'{k} : {v}')
                else:
                    print(f'{k} :     ')
            continue
    # After parsing for movements, check if the user wishes to exit and break while loop if true
    if 'Exit' in tokens:
        break

    # Check that the user has input a valid command.
    # If valid_tokens contains zero elements then the user has input an invalid command.
    # print out a notification letting the user know, then wait before returning to the while loop
    elif len(valid_tokens) == 0:
        print('\nNot a valid command, try again. \n')
        sleep(1.5)

# If while loop is broken, clear screen and print some gratitude.
os.system('cls')
print('\n  Thanks for playing! \n \n')