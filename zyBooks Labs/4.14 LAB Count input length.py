#Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

#Ex: If the input is:

#Listen, Mr. Jones, calm down.
#the output is:

#21
#Note: Account for all characters that aren't spaces, periods, or commas (Ex: "r", "2", "!").

###########################################

# take user input and assign to user_test
# create a set of ignored characters as null_char
# create variable as 'char_count' assigned to 0, this will increment with all string characters not in the null_char set

user_text = input()
null_char = {' ', '.', ','}
char_count = 0

# Iterate over user_text using a for loop
for ch in user_text:
    # check if character is in null_char
    if ch in null_char: 
        continue  # if True, continue loop
    else:
        count += 1 #if False, add 1 to char_count

# print the final count of accepted characters        
print(count)