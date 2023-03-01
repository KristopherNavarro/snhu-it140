from datetime import datetime

repeat = 'y'

while (repeat == 'y'):
    name = input('What is your name? ')
    age = int(input('What is your age? '))

    current_year = int(datetime.now().year)

    year_born = current_year - age

    print(f'''
Hello, {name}! You were born in {year_born}.
    ''')
    repeat = input('Run again? y/n ')

print('That was fun!')
