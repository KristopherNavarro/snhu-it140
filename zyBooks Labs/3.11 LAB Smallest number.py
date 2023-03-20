# Write a program whose inputs are three integers, and
# whose output is the smallest of the three values.
#
#   Ex:     If the input is:    7
#                               15
#                               3
#           the output is:      3
#
##################################################################

# User will input three integer variables,
# the largest number of the three variables is printed.


# Create three variables named input1, input2, and input3. Each variable
# will pass a user input() to the int() function.
input1 = int(input())
input2 = int(input())
input3 = int(input())

# Create a list named input_list that contains input1, input2, and input3
input_list = [input1, input2, input3]

# Create a variable named max_input that passes input_list to min()
max_input = min(input_list)

# Print max_input
print(max_input)

################################################################
#   OUTCOME: PASS 10/10