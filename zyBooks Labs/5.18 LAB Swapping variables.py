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

# Define function named swap_values that takes two arguments, var1 and var2.
# This function creates a list with var1 and var2 in reverse order, assigned to values
def swap_values(var1, var2):
    values = [var2, var1]
    return(values[0], values[1])


# if statement supplied by test environment
if __name__ == '__main__':
    
    # Retreive two inputs from user, user_var1 and user_var2
    # pass both variables to swap_values() in the same order
    # received, assigned to variables t1 and t2 simultaneously
    user_var1 = input()
    user_var2 = input()
    t1, t2 = swap_values(user_var1, user_var2)

    # print t1 and t2
    print(t1, t2)

###############################################################################3
# GRADE: 10/10