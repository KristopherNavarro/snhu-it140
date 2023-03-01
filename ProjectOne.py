from datetime import datetime

ask_name = input('What is your name? ')
ask_age = int(input('What is your age? '))

name = copy(ask_name)
age = copy(ask_age)
current_year = int(datetime.now().year)

year_born = current_year - age

print(f'''
Hello, {name}! You were born in {year_born}.''')
