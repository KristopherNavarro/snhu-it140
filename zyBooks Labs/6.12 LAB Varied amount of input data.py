# Statistics are often calculated with varying amounts
# of input data. Write a program that takes any number
# of integers as input, and outputs the average and max.
#
# Ex:   If the input is:    15 20 0 5
#       the output is:      10 20
#
##########################################################

# receive user input of unknown quantity of variables
user_input = input()

# use list comprehension to parse variables and conver to integers
tokens = [int(i) for i in user_input.split()]

# assign variables for the average and max of user_input, then print
avg_tokens = int(sum(tokens) / len(tokens))
max_tokens = max(tokens)

print(avg_tokens, max_tokens)

#################################################
# RESULT: 10/10
