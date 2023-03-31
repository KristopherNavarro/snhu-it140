# Write a program whose input is two integers and
# whose output is the two integers swapped.
#
# Ex: If the input is:  3
#                       8
#     the output is:    8 3
#
# Your program must define and call the following function. swap_values()
# returns the two values in swapped order.
#
# def swap_values(user_val1, user_val2)
#
#############################################################################


# Define function named swap_values that takes an unknown quantity of arguments.
# This function creates an empty list variable, then loops through all arguments, appending each to the list.
def swap_values(*args):
    values = []
    for v in args:
        values.append(v)
    
    # reverse the list and print the first two values.
    values.reverse()
    print(values[0],values[1])

# if dunder name equals dunder main supplied by test environment 
if __name__ == '__main__':
    
    # Retreive two input values assigned to val1 and val2, pass variables to swap_values()
    val1 = input()
    val2 = input()
        
    swap_values(val1, val2)

# Write a program whose input is two integers and
# whose output is the two integers swapped.
#
# Ex: If the input is:  3
#                       8
#     the output is:    8 3
#
# Your program must define and call the following function. swap_values()
# returns the two values in swapped order.
#
# def swap_values(user_val1, user_val2)
#
#############################################################################

<<<<<<< main

# Define function named swap_values that takes an unknown quantity of arguments.
# This function creates an empty list variable, then loops through all arguments, appending each to the list.
def swap_values(*args):
    values = []
    for v in args:
        values.append(v)
    
    # reverse the list and print the first two values.
    values.reverse()
    print(values[0],values[1])

# if dunder name equals dunder main supplied by test environment 
if __name__ == '__main__':
    
    # Retreive two input values assigned to val1 and val2, pass variables to swap_values()
    val1 = input()
    val2 = input()
        
    swap_values(val1, val2)

