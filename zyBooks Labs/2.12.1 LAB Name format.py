# User inputs firstName middleName lastName (in one line)
# Print lastName, firstInitial.middleInitial.
# If user inputs firstName lastName (in one line)
# Print lastName, firstInitial.

# Take user input and split to create a list
user = input().split()

# If
if len(user) == 3:
    firstName = user[0]
    middleName = user[1]
    lastName = user[2]
    print(f'{lastName.title()}, {firstName[0].upper()}.{middleName[0].upper()}.')
else:
    firstName = user[0]
    lastName = user[1]
    print(f'{lastName.title()}, {firstName[0].upper()}.')
