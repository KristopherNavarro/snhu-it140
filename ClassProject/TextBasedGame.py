# Created by:   Kristopher Navarro
# GitHub repo:  https://github.com/KristopherNavarro/snhu-it140
# Class:        SNHU IT-140-J4175
# Instructor:   Patrick Moore
# Term:         23EW4
# Date:         16 April 2023
#
###########################################################################

# import packages to clean up gameplay and add some flair.
# 'os' is used for clearing the screen often
# 'sleep' is used to delay 'os' in most cases
# 'random' is only used to select from the bad_moves list
# 'uniform' is used in the Typewriter class for visualization.
import os
from time import sleep
import random as random
from random import uniform

# def secrets(item):            # Unused in this deployment, for future use.
#     secrets_map = {
#         'Servant Quarters': 'Hidden Room',
#         'Office': 'Secret Passage'}
#     for v in inventory.values():
#         if v == item:
#             return secrets_map[current_room]
#         elif len(breadcrumbs) > 0:
#             return breadcrumbs[-1]

# Primary variables for basic functions
health = 2      # Starting lives, chances to face the demon. Decrements if pages != 6
pages = 0       # increments with ever book page collected
current_room = 'Entry'      # stores the value for current room from movement
breadcrumbs = []            # stores previous rooms in order
moves = 0                   # increments with ever valid move
vanquished = False          # used to break the gameplay loop if user has 6 pages when entering the attic
describe_the_room = False   # used to printing the room_description value
# inventory = {1: '',       # unused variable, for future deployment
#              2: '',
#              3: '',
#              4: '',
#              5: '',
#              6: '',}

# map is a dictionary of the room layout
map = {
    # First Floor

    'Entry': {
        'Enter': 'Grand Hall',
        'North': 'Grand Hall',},
    'Lounge': {
        'North': 'Dining Room',
        'East': 'Grand Hall'},
    'Grand Hall': {
        'Ascend': '2nd Floor Landing',
        'Climb': '2nd Floor Landing',
        'Stairs': '2nd Floor Landing',
        'Upstairs': '2nd Floor Landing',
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
        'East': 'Stairwell',
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
        'West': 'Garden'},
    'Hedge Maze': {
        'North': 'Graveyard',
        'South': 'Garden'},
    'Graveyard': {
        'South': 'Hedge Maze'},
    'Hidden Room': {
        'West': 'Servant Quarters'},

    #Second Floor

    'Game Room': {
        'East': '2nd Floor Landing'},
    '2nd Floor Landing': {
        'North': 'Den',
        'East': 'Upstairs Hall',
        'West': 'Game Room',
        'Down': 'Grand Hall',
        'Descend': 'Grand Hall',
        'Stairs': 'Grand Hall',
        'Downstairs': 'Grand Hall'},
    'Upstairs Hall': {
        'North': 'Master Suite',
        'South': 'Guest Room',
        'West': '2nd Floor Landing',
        'East': 'Stairwell'},
    'Guest Room': {
        'North': 'Upstairs Hall'},
    'Den': {
        'South': '2nd Floor Landing'},
    'Master Suite': {
        'South': 'Upstairs Hall'},

    # Third floor

    'Attic': {
        'South': 'Altar',
        'East': 'Stairwell'},
    'Altar': {
        'North': 'Attic',
        'Trap Door': 'Grand Hall'}
    }
# map_items is a dictionary of items per room with validation key:value pairs
map_items = {
    'Servant Quarters': {
        'available': True,
        'item': 'Page 1',
        'page': True,
        'observed': False},
    'Den': {
        'available': True,
        'item': 'Page 2',
        'page': True,
        'observed': False},
    'Graveyard': {
        'available': True,
        'item': 'Page 3',
        'page': True,
        'observed': False},
    'Kitchen': {
        'available': True,
        'item': 'Page 4',
        'page': True,
        'observed': False},
    'Office': {
        'available': True,
        'item': 'Page 5',
        'page': True,
        'observed': False},
    'Guest Room': {
        'available': True,
        'item': 'Page 6',
        'page': True,
        'observed': False},
    }
# a dictionary containing the descriptions for each room
room_descriptions = {
    'Entry': '''      You are in the Entry of Marrowood, there is only 
  one direction to go.
__________________________________________________________''',
    'Grand Hall': '''      The Grand Hall is illuminated from the evening's 
  full Moon. Before you is a Grand Staircase.
__________________________________________________________''',
    'Lounge': '''      This room has a faint scent of tobacco. There are
  furniture pieces meant for long conversations.
__________________________________________________________''',
    'Library': '''      The scent of old paper engulfs you. The walls are
  lined with more books than most people would ever read
  in a lifetime. 
__________________________________________________________''',
    'Office': '''      Papers are strewn across a large wooden desk in 
  the middle of the room. One paper looks much older 
  than all of the others... 
__________________________________________________________''',
    'Dining Room': '''      A long and opulent room, with a table to match. 
  Plates with food scraps have not been cleared, chairs
  are knocked over and out of place.
__________________________________________________________''',
    'Kitchen': '''      This room is in wild disarray. Drawers pulled out, 
  cutlery is all over the place. In the mess, something 
  old catches your eye...
__________________________________________________________''',
    'Pantry': '''      The shelves are nearly bare. The new tenants may 
  have over extended themselves, in more than one way.
__________________________________________________________''',
    'Servant Hall': '''      The hairs on your neck begin to stand on end. The 
  air feels strange here. There is a Stairwell toward 
  the East.
__________________________________________________________''',
    'Sun Room': '''      Tonight, this is a Moon Room. You are bathed in 
  the light of the full Moon. What else could be possible
  tonight?
__________________________________________________________''',
    'Garden': '''      Outside on the vast estate grounds. In the 
  moonlight you see strange shrubbery to the North.
__________________________________________________________''',
    'Servant Quarters': '''      Chills reverberate down your spine. There is 
  something unsettling about this room. As you turn to 
  leave, something catches your eye...
__________________________________________________________''',
    'Hidden Room': '''      What was this place? There are stains and gouges 
  on the walls. 
__________________________________________________________''',
    'Hedge Maze': '''      The legendary Marrowood Hedge Maze has fallen to a 
  state of disrepair, making it easy to see a path 
  through. But a path is not all you see, there is 
  something to the North. 
__________________________________________________________''',
    'Graveyard': '''      The rumors were true, this is the Marrowood Family 
  Cemetary. As you meander through the headstones you 
  step on something...
__________________________________________________________''',

    # 2nd floor

    'Game Room': '''      At one time this room entertained men of importance
  from around the country. At this time it entertains
  vacancy. The room is empty.
__________________________________________________________''',
    'Den': '''      This room is the sanctuary away from the business
  of the socialites. In the dim light you see something
  protruding from a vent... 
__________________________________________________________''',
    '2nd Floor Landing': '''
      A long balcony overlooking the Grand Hall, the main
  connection between the entertaining wing and the 
  sleeping quarters.  
__________________________________________________________''',
    'Upstairs Hall': '''      This hall connects the sleeping quarters for 
  masters and guests, lined with reminders of grandeur. 
  There is a Stairwell toward the East.
__________________________________________________________''',
    'Guest Room': '''      Many regal guests have stayed in this room. There 
  are rumors of hidden compartment throughout its wood 
  floors and elaborate panelling. But, there is something
  else that has your attention...
__________________________________________________________''',
    'Master Suite': '''      If these walls could talk. There is a fully stuffed
  lion and ewe on one end of the room. 
__________________________________________________________''',

    # 3rd Floor

    'Attic': '''
      Crates, thick dust, and cobwebs obscure the 
  labrynth that is the Attic. The air is thick and spells
  fresh and ancient at the same time. You must be close.  
__________________________________________________________''',
    'Stairwell': '''
      You are in the East Stairwell. Only way to go is 
  up or down... or back the way you came.
__________________________________________________________''',
}
# a list of decline responses for invalid moves
bad_moves = [
    'Only ghosts can walk through walls, try again.',
    'Your vision may be sharp, but not your sight, try again.',
    'Too much of that and we\'ll all be lost, try again.',
    'Something is amiss, try again.',
    'You won\'t vanquish much in that direction, try again.',
    'Something went bump in the night, it was you. Try again.',
    'Not all who wonder are lost, but you surely are. Try again.'
]

# the following sets contain possible responses for movement, heading, action, and observation
movement_keys = {'Go', 'Move', 'Head', 'Travel', 'Step', 'Trek', 'Advance',
                 'Proceed', 'Run', 'Walk', 'Crawl', 'Climb', 'Descend', 'Ascend'}
heading_keys = {'North', 'South', 'East', 'West', 'Up', 'Down', 'Descend', 'Ascend',
                'Staircase', 'Enter', 'Stairs', 'Upstairs', 'Downstairs'}
action_keys = {'Get', 'Take', 'Grab', 'Acquire', 'Obtain'}
observation_keys = {'Look', 'See', 'Examine', 'Observe', 'Inspect', 'Scan'}


# Typewriter is for visualization purposes. See docstring for more info:
class Typewriter:
    ''' Iterates over a string and prints with a varying pause between each character to mimmick a typewriter.

    --slow(self, stop=''):
        takes a string and stop value as arguments, stop is automatically set to an empty string
        prints at a slow speed

    -- med(self, stop=''):
        takes a string and stop value as arguments, stop is automatically set to an empty string
        prints at a medium speed

    -- fast(self, stop=''):
        takes a string and stop value as arguments, stop is automatically set to an empty string
        prints at a fast speed

    '''

    def slow(self, stop=''):
        for ch in self[:-1]:
            print(ch, end='', flush=True)
            sleep(uniform(0.1, 0.25))
        print(self[-1], end=stop, flush=True)

    def med(self, stop=''):
        for ch in self[:-1]:
            print(ch, end='', flush=True)
            sleep(uniform(0.005, 0.1))
        print(self[-1], end=stop, flush=True)

    def fast(self, stop=''):
        for ch in self[:-1]:
            print(ch, end='', flush=True)
            sleep(uniform(0.001, 0.01))
        print(self[-1], end=stop, flush=True)


# used for cleaning up visualizations. See docstring for more info.
def centered(*args, spaces):
    ''' Concatenates multiple arguments and centers based on the supplied total space width as spaces'''
    arg_list = []
    for arg in args:
        arg_list.append(str(arg))
    text = ''.join(arg_list)
    return text.center(spaces)

# This is used to clean up code space and create 'slides' for an introduction. Mostly just simple visuals.
def introduction():
    os.system('cls')
    print(r'''
  <@)>^-^-    Welcome to Marrowood Mansion!    -^-^-<(@>
__________________________________________________________
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
    sleep(1.1)
    input('                     Press ENTER...')

    os.system('cls')
    print('''
  <@)>^-^-    Welcome to Marrowood Mansion!    -^-^-<(@>
__________________________________________________________
''')
    Typewriter.fast('''
      Something wicked was conjured in Marrowood... 

      A lively and bright dinner party, hosted by the 
  new owners of the Marrowood Estate, has taken a sinister 
  turn when curiosities became insatiable... 

''')
    sleep(1.1)
    input('                Press ENTER to continue...')

    os.system('cls')
    print('''
  <@)>^-^-    Welcome to Marrowood Mansion!    -^-^-<(@>
__________________________________________________________
''')
    Typewriter.fast('''      While exploring the residence, a long-rumored 
   Altar Room was discovered, along with an ancient
   book: 

  <@)>--^~-   The Grimoire of Pope Honorius   -^-`^-<(@>  

      Ignorant of the power the spells within possessed, 
  the party has unleashed a demonic being upon our world. 
  The demon has retreated to the Altar room after chasing 
  the party guests from the house. 
      In the mayhem to escape the demon... 

  <@)>-^-^--~--   SIX PAGES WERE LOST    -^-~-^-`^-<(@>

''')
    sleep(1.1)
    input('             Press ENTER to continue...')

    os.system('cls')
    print('''
  <@)>^-^-    Welcome to Marrowood Mansion!    -^-^-<(@>
__________________________________________________________
''')
    Typewriter.fast('''
      Your quest is to find the missing pages scattered
  throughout the mansion before making your way to the 
  Altar Room to vanquish the demon lurking within.

      You begin your quest in the Entry of Marrowood, 
  armed only with your wit, a bag, and the incomplete 
  Grimoire of Pope Honorius... 
                                -~^-~-^-`^-<(@

''')
    sleep(1.1)
    input('                Press ENTER to begin...')


# This is the primary header visual for the game. Takes one string argument.
def display_header(arg):
    os.system('cls')            # This will keep the screen clean
    var = 'You are in the '     # required for the centered() function

    print(f'''
  @)>^-~-`- {centered(var, arg, spaces=33)} -~^-`^-<(@
__________________________________________________________
    Moves [{centered(moves, spaces=3)} ]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
---------------------------------------------------------- ''', flush=True)


# simple slide based visualization for the Help screen, describes gameplay
def help_menu():
    display_header('HELP')
    print('''  Navigating Rooms--                
      Enter commands like 'move', 'go', 'walk', etc., 
      along with a cardinal direction.
      [ EX:  move east  ] 
        
  Navigating Stairs--  
      Use commands like 'go', 'climb', 'head', etc., 
      along with the stair direction you wish to go. 
      [ EX:  climb the stairs  ]
                                                    1 of 3  
__________________________________________________________''', flush=True)
    input('                Press ENTER to continue...')

    display_header('HELP')
    print('''  Observing--                
      Commands like 'look', 'inspect', 'scan', etc.
      [ EX:  inspect the room  ]
      [      look at the room  ]

  Actions--
      Commands like 'take', 'get', 'grab', etc.
      [ EX:  grab the page  ]
      [      acquire page   ]
                                                    2 of 3
__________________________________________________________''', flush=True)
    input('                Press ENTER to continue...')

    display_header('HELP')
    print('''  Gameplay--               
      You have 2 lives.
      
      You must collect all 6 pages before facing the 
        demon, or suffer the consequences.
      
      Pages are only visible if you look for them.
      
      Type 'help' to get these instructions again.
                                                    3 of 3
__________________________________________________________''', flush=True)
    input('                Press ENTER to continue...')


# This handles looking around a room, retrieving values from room_descriptions, as well as validating
# retrievable items have been observed first before being able to be retrieved. Initiated by an if
# statement looking for describe_the_room == True
def room_observation(room):
    global map_items
    global describe_the_room

    # prints the appropriate room_description value
    print('\n', room_descriptions[room], '\n', flush=True)
    describe_the_room = False       # resets to False

    # Checks if there is an available item in the room
    # prints validation if item is present
    try:
        if map_items[room]['available'] == False:
            print('  There is nothing to see here.','\n', flush=True)

        else:
            map_items[room]['observed'] = True
            sleep(2)
            print(f'  You found a page!', '\n', flush=True)
            sleep(1)

    # Handles any KeyErrors by ignoring and moving on
    except KeyError:
        pass
    pass


# This handles all gameplay movements around the map, takes one argument
def movement(token):
    global current_room
    global moves

    last_room = current_room        # stores a copy of current_room

    # Sub-function that takes care of the issues of traversing between floors via the map Stairwell
    # takes one argument
    def stairs(arg):
        global current_room

        # Internal dictionary, maps movement via Stairwell
        stairwell = {'floor1': {
                        'West': 'Servant Hall',
                        'Up': 'Upstairs Hall',
                        'Upstairs': 'Upstairs Hall',
                        'Ascend': 'Upstairs Hall',
                        'Climb': 'Upstairs Hall'},
                    'floor2': {
                        'West': 'Upstairs Hall',
                        'Up': 'Attic',
                        'Upstairs': 'Attic',
                        'Ascend': 'Attic',
                        'Climb': 'Attic',
                        'Down': 'Servant Hall',
                        'Downstairs': 'Servant Hall',
                        'Descend': 'Servant Hall'},
                    'floor3': {
                        'West': 'Attic',
                        'Down': 'Upstairs Hall',
                        'Downstairs': 'Upstairs Hall',
                        'Descend': 'Upstairs Hall'}
                    }

        # Validates which floor the user is on and handles the stairs accordingly
        try:
            if breadcrumbs[-1] == 'Servant Hall':
                current_room = stairwell['floor1'][arg]

            elif breadcrumbs[-1] == 'Upstairs Hall':
                current_room = stairwell['floor2'][arg]

            elif breadcrumbs[-1] == 'Attic':
                current_room = stairwell['floor3'][arg]
        except KeyError:
            return KeyError     # if KeyError is raised, returns to parent function

    # Sub-function that validates whether all pages have been collected
    # takes one argument
    def all_pages(arg):
        global health
        global current_room
        global vanquished
        global moves

        moves += 1      # increments moves

        # returns the user to the Grand Hall if pages != 6 and lives > 1
        if pages != 6 and health > 1:
            health -= 1     # decrements health

            # Moves user to Attic for theatrical purpose, prints explanation and warning
            current_room = map[current_room][arg]
            display_header(current_room)
            print(f'''        As you search the pages for the incantations you 
  realize there are pages still missing. The demon lunges 
  toward you but you evade, and discover a trap door and 
  make your escape! 
      
      You find yourself back in the {map[current_room]['Trap Door']}. 
      
      Next time you won't be so lucky...
__________________________________________________________''', flush=True)
            input('                Press ENTER to continue...')     # waits for user input to continue
            current_room = map[current_room]['Trap Door']           # returns user to Grand Hall
        elif pages != 6 and health == 1:
            health -= 1     # decrements health to zero, result: breaking the gameplay loop, defeat screen displayed
            pass
        # if pages equals 6 then loop is broken by vanquished == True, victory screen is displayed
        elif pages == 6 and health > 0:
            vanquished = True
            pass

    # Main movement function, checks if the current room is Stairwell or Attic and applies
    # the correct sub-function
    try:
        if current_room == 'Stairwell':
            stairs(list(token)[0])
        elif current_room == 'Attic':
            all_pages(list(token)[0])
        else:
            current_room = map[current_room][list(token)[0]]
            moves += 1
            breadcrumbs.append(last_room)

    # if movement is invalid resulting in a KeyError, prints a random response from bad_moves
    except KeyError:
        print(f'\n{random.choice(bad_moves)} \n', flush=True)
        sleep(2)
    pass

# def hedge_maze():       # unused in this deployment,
#     ''' not yet defined, future addition
#     In a future iteration this will handle either a sub-map or shifting directions to disorient the user'''
#     pass

# This handles the action tasks. i.e. taking items
def act():
    global map_items
    global pages

    # try block in case of KeyError
    try:
        # Checks map_items for current_room and if item has been observed
        # If not observed, prints directions to user
        if map_items[current_room]['observed'] == False:
            print('\n','  Try looking around first.', flush=True)
            sleep(2)
            pass
        # if already observed, checks if item is available to be taken
        # if available, increments pages by 1 and sets availability of item to False
        elif map_items[current_room]['available'] == True:
            pages += 1
            map_items[current_room]['available'] = False

            # prints the display_header and confirmation of which page was acquired
            display_header(current_room)
            print(f'  You have {map_items[current_room]["item"]}!...',end='', flush=True)

            # if statment that informs the user of remaining pages, if any
            if 6 - pages == 1:
                print(f'  {6 - pages} page left.', flush=True)
            elif 6- pages == 0:
                print(f'  You have all the pages, head to the Altar!', flush=True)
            else:
                print(f'  {6 - pages} pages left.', flush=True)
            sleep(2.5)
        # else item has been taken or no item present, informs user with a printout.
        else:
            print('  There is nothing to take.', flush=True)
            sleep(1.5)
    # If here is a KeyError, then there is no item
    except KeyError:
        print('  There is nothing to take.', flush=True)
        sleep(1.5)
    pass

if __name__ == '__main__':

    introduction()      # call to introduction(), displays intro slides for user

    help_menu()         # call to help_menu(), displays gameplay info for user

    # Begin the while loop, continue as long as health is greater than zero
    while health > 0:
        if vanquished == True:  # Breaks loop if user has acquired all pages and current_room is Attic
            break

        # prints out the main display_header with passed current_room
        display_header(current_room)

        # checks if the room_description value is needed, prints if it is.
        if describe_the_room == True:
            if current_room == 'Stairwell':
                pass
            room_observation(current_room)

        # requests direction from user, formats as a string, titlecase, and splits into a list.
        user_input = str(input('What would you like to do? ')).title().split()

        # compares user_input to gameplay sets, parses accordingly by heading, observation, or action
        heading = list(set(user_input) & heading_keys)
        observe = list(set(user_input) & observation_keys)
        action = list(set(user_input) & action_keys)

        # checks if user entered Quit or Exit, ends gameplay by breaking loop
        if 'Quit' in user_input or 'Exit' in user_input:
            break
        elif 'Help' in user_input:      # calls help_menu if user enters Help
            help_menu()
        elif len(heading) > 0:          # call for movement() if user has entered movement_keys
            movement(heading)
        elif len(observe) > 0:
            describe_the_room = True    # sets describe_the_room to True if user entered observation_keys
        elif len(action) > 0:
            act()                       # call for act() if user entered action_keys

        # if user entered an invalid command then alerts user and continues loop
        else:
            print('\n  I don\'t understand. Try again.', flush=True)
            sleep(1.5)
        continue

    # Loop is broken: Checks for how end screen should display

    if health == 0:             # User was defeated
        os.system('cls')
        print(f'''
      @)>^-~-`- {centered('Thank you for playing!', spaces=33)} -~^-`^-<(@
    __________________________________________________________
        Moves [{centered(moves, spaces=3)} ]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
    ---------------------------------------------------------- 
    ''')
        Typewriter.fast('''      With pages still missing, the spells you require 
      are incomplete. Your weak attempts to attack the demon 
      only antagonize it, and it devours you.
                      
                      Better luck next time!
    
                @)>^-~^-`^-~-- .... --^-~^-~`^-<(@
    
    
    ''')

    elif vanquished == True:        # User was successful
        os.system('cls')
        print(f'''
      @)>^-~-`- {centered('Thank you for playing!', spaces=33)} -~^-`^-<(@
    __________________________________________________________
        Moves [{centered(moves, spaces=3)} ]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
    ---------------------------------------------------------- 
    ''')
        Typewriter.fast('''      With the complete Grimoire of Pope Honorius, your 
      incantations cast the demon back to the Netherworld!
    
    
           @)>^-~^-`^-~--   YOU WIN!   --^-~^-~`^-<(@
    
    
    
    ''')

    else:                       # User ended game voluntarily
        os.system('cls')
        print(f'''
      @)>^-~-`- {centered('Goodbye!', spaces=33)} -~^-`^-<(@
    __________________________________________________________
        Moves [{centered(moves, spaces=3)} ]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
    ---------------------------------------------------------- 
    ''')
        Typewriter.fast('''                  Thank you for playing!
    
                @)>^-~^-`^-~-- .... --^-~^-~`^-<(@
     
    
    
    ''')