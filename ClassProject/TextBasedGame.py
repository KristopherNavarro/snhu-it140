# Room layout for Text Based Game

import os
from time import sleep
import random as random
from random import uniform

# def secrets(item):
#     secrets_map = {
#         'Servant Quarters': 'Hidden Room',
#         'Office': 'Secret Passage'}
#     for v in inventory.values():
#         if v == item:
#             return secrets_map[current_room]
#         elif len(breadcrumbs) > 0:
#             return breadcrumbs[-1]


health = 2  # Starting health, chances to face the Boss
pages = 0  # increments with ever book page collected
current_room = 'Entry'
breadcrumbs = []
moves = 0
inventory = {
    'Slot 1': '',
    'Slot 2': '',
    'Slot 3': ''}
vanquished = False

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
        'Descend': 'Grand Hall'},
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
room_descriptions = {
    'Entry': '''    You are in the Entry of Marrowood 
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
bad_moves = [
    'Only ghosts can walk through walls, try again.',
    'Your vision may be sharp, but not your sight, try again.',
    'Too much of that and we\'ll all be lost, try again.',
    'Something is amiss, try again.',
    'You won\'t vanquish much in that direction, try again.'
]

movement_keys = {'Go', 'Move', 'Head', 'Travel', 'Step', 'Trek', 'Advance', 'Proceed', 'Run', 'Walk', 'Crawl', 'Climb', 'Descend', 'Ascend'}
heading_keys = {'North', 'South', 'East', 'West', 'Up', 'Down', 'Descend', 'Ascend', 'Staircase', 'Enter'}
action_keys = {'Get', 'Take', 'Grab'}
observation_keys = {'Look', 'See', 'Examine'}





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

    def slow(self, stop=''):
        global variability
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

def centered(*args, spaces):
    ''' Concatenates multiple arguments and centers based on the supplied totoal space width as spaces'''
    arg_list = []
    for arg in args:
        arg_list.append(str(arg))
    text = ''.join(arg_list)
    return text.center(spaces)

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
    sleep(1.1)
    print('''
                     Press ENTER...''', end='')
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
    sleep(1.1)
    print('''                Press ENTER to continue...''', end='')
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
    sleep(1.1)
    print('''
                Press ENTER to continue...''', end='')
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
    sleep(1.1)
    print('''
                Press ENTER to begin...''', end='')
    input()

def display_header(arg):
    os.system('cls')  # This will keep the screen clean
    var = 'You are in the '

    print(f'''
  @)>^-~-`- {centered(var, arg, spaces=33)} -~^-`^-<(@
__________________________________________________________
    Moves [{centered(moves, spaces=3)} ]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
---------------------------------------------------------- ''', flush=True)

def help():
    display_header()
    print('''
  This is the help filler...
    ''')
    input()
    pass

def room_observation():
    try:
        print('\n',room_descriptions[current_room])
        input('                Press ENTER to continue...')
    except KeyError:
        return ''

def movement(token):
    global current_room
    global moves

    last_room = current_room

    def stairs(arg):
        global current_room
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
        try:
            if breadcrumbs[-1] == 'Servant Hall':
                current_room = stairwell['floor1'][arg]

            elif breadcrumbs[-1] == 'Upstairs Hall':
                current_room = stairwell['floor2'][arg]

            elif breadcrumbs[-1] == 'Attic':
                current_room = stairwell['floor3'][arg]
        except KeyError:
            return KeyError

    def all_pages(arg):
        global health
        global current_room
        global vanquished
        global moves

        moves += 1

        if pages != 6 and health > 1:
            health -= 1

            current_room = map[current_room][arg]
            display_header(current_room)
            print(f'''        As you search the pages for the incantations you 
  realize there are pages still missing. The demon lunges 
  toward you but you evade, and discover a trap door and 
  make your escape! 
      
      You find yourself back in the {map[current_room]['Trap Door']}. 
      
      Next time you won't be so lucky...
__________________________________________________________''')
            input('                Press ENTER to continue...')
            current_room = map[current_room]['Trap Door']
        elif health <= 1:
            health -= 1
            pass
        elif pages == 6 and health > 0:
            vanquished = True
            pass

    try:
        if current_room == 'Stairwell':
            stairs(list(token)[0])
        elif current_room == 'Attic':
            all_pages(list(token)[0])
        else:
            current_room = map[current_room][list(token)[0]]
            moves += 1
            breadcrumbs.append(last_room)

    except KeyError:
        print(f'\n{random.choice(bad_moves)} \n')
        sleep(2)
    pass

def view():
    global map_items

    #room_observation()

    try:
        if map_items[current_room]['available'] == False:
            print('  There is nothing to see here.')
            sleep(1.5)
        else:
            map_items[current_room]['observed'] = True
            print(f'  You found a page!')
            sleep(1.8)
    except KeyError:
        pass
    pass

def act():
    global map_items
    global pages
    try:
        if map_items[current_room]['observed'] == False:
            print('  Try looking around first.')
            sleep(2)
            pass
        elif map_items[current_room]['available'] == True:
            pages += 1
            map_items[current_room]['available'] = False

            print(f'  You now have {map_items[current_room]["item"]}!')

            if 6 - pages == 1:
                print(f'  There is {6 - pages} page left!')
            elif 6- pages == 0:
                print(f'  There are {6 - pages} pages left! Head to the Altar Room!')
            else:
                print(f'  There are {6 - pages} pages left to find.')
            sleep(3.3)
        else:
            print('  There is nothing here.')
            sleep(1.5)
    except KeyError:
        print('  There is nothing to here.')
        sleep(1.5)
    pass


# introduction()

while health > 0:
    if vanquished == True:
        break

    display_header(current_room)

    user_input = str(input('What would you like to do? ')).title().split()

    heading = list(set(user_input) & heading_keys)
    observe = list(set(user_input) & observation_keys)
    action = list(set(user_input) & action_keys)

    if 'Quit' in user_input:
        break
    elif 'Help' in user_input:
        help()
    elif len(heading) > 0:
        movement(heading)
    elif len(observe) > 0:
        view()
    elif len(action) > 0:
        act()
    else:
        print('\n I don\'t understand. Try again.')
        sleep(1.5)

if health == 0:
    os.system('cls')
    print(f'''
  @)>^-~-`- {centered('Thank you for playing!', spaces=33)} -~^-`^-<(@
__________________________________________________________
    Moves [{centered(moves, spaces=3)} ]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
---------------------------------------------------------- 

      With pages still missing, the spells you require 
  are incomplete. Your weak attempts to attack the demon 
  only antagonize it, and it devours you.
                  
                  Better luck next time!

            @)>^-~^-`^-~-- .... --^-~^-~`^-<(@

__________________________________________________________ 
''', flush=True)
elif vanquished == True:
    print(f'''
  @)>^-~-`- {centered('Thank you for playing!', spaces=33)} -~^-`^-<(@
__________________________________________________________
    Moves [{centered(moves, spaces=3)} ]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
---------------------------------------------------------- 


      With the complete Grimoire of Pope Honorius, your 
  incantations cast the demon back to the Netherworld!


           @)>^-~^-`^-~-- YOU WIN! --^-~^-~`^-<(@


__________________________________________________________''')


else:
    os.system('cls')
    print(f'''
  @)>^-~-`- {centered('Goodbye!', spaces=33)} -~^-`^-<(@
__________________________________________________________
    Moves [{centered(moves, spaces=3)} ]    ---<--< {'{:<2}'.format('*' * health)} >-->----    Pages [{centered(pages, spaces=3)}]
---------------------------------------------------------- 

                
                  Thank you for playing!

            @)>^-~^-`^-~-- .... --^-~^-~`^-<(@


__________________________________________________________ 
''', flush=True)