# Created by: Kristopher Navarro

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
map = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

items = {
        'Great Hall': {
            'item': 'Torch',
            'observed': False },
        'Bedroom': {
            'item': 'Pillow',
            'observed': False },
        'Cellar': {
            'item': 'Axe',
            'observed': False }
}
movement_verbs = ('Go', 'Move', 'Head')
action_verbs = ('Get', 'Take', 'Grab')
obs_verbs = ('Look', 'See', 'Examine')
directions = ('North', 'South', 'East', 'West', 'Up', 'Down')

current_room = 'Great Hall'
inventory = {
        'slot 1': False,
        'slot 2': False,
        'slot 3': False,
}

print('''
Welcome to the Mansion!
''')

while True:
    user_input = str(input('What would you like to do? \n')).title()
    tokens = user_input.split()
    for token in tokens:
        if token in movement_verbs:
            for token in tokens:
                if token in directions:
                    try:
                        current_room = map[current_room][token]
                        print(f'You are now in the {current_room}.')
                    except KeyError:
                        print('Only ghosts can walk through walls, try again.')
            continue
        elif token in obs_verbs:
            if items[current_room]['item'] == False:
                print('There is nothing here.')
            else:
                items[current_room]['observed'] = True
                print(f'You see a {items[current_room]["item"]}')
            continue
        elif token in action_verbs:
            if items[current_room]['observed'] == False:
                print('There is nothing to take, try looking around.')
                continue
            else:
                new_inventory = items[current_room]['item']
                for k,v in inventory.items():
                    if v == False:
                        inventory[k] = items[current_room]['item']
                        items[current_room]['item'] = False
                print(f'You now have the {new_inventory}.')
            continue

        elif token == 'Inventory':
            for k,v in inventory.items():
                if v != False:
                    print(f'{k} : {v}')
                else:
                    print(f'{k} :     ')
            continue
        #print('That was an invalid command, try again.')
    if 'Quit' in tokens:
        break

print('Thanks for playing!')

