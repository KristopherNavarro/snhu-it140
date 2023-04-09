# Write a program that gets a list of integers from input, and
# outputs non-negative integers in ascending order (lowest to highest).
#
# Ex:   If the input is:    10 -7 4 39 -6 12 2
#       the output is:      2 4 10 12 39
#
# For coding simplicity, follow every output value by a space. Do not end with newline.
#
#######################################################################################

# receive user input of unknown quantity of variables
user_input = input()

# use list comprehension to parse variables and convert to integers
tokens = [int(i) for i in user_input.split()]

# use another list comprehension to only add positive numbers
# pass comprehension to the sorted() function.
pos_tokens = sorted([i for i in tokens if i >= 0])

# print result
for token in pos_tokens:
    print(token, end=' ')

#######################################################################################
# RESULT: 10/10