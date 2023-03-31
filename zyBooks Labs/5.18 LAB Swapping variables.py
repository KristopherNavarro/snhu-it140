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

def swap_values(*args):
    values = []
    for v in args:
        values.append(v)

    values.reverse()
    return (values[0],values[1])


# val1 = input()
# val2 = input()
#
# rval1, rval2 = swap_values(val1, val2)
#
# print(rval1, rval2)

# The max grade I am receiving is 8/10.