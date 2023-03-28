# Write a program with total change amount as an integer input that
# outputs the change using the fewest coins, one coin type per line.
# The coin types are dollars, quarters, dimes, nickels, and pennies.
# Use singular and plural coin names as appropriate, like 1 penny vs.
# 2 pennies.
#
# Ex: If the input is:    0 or less,
#     the output is:      no change
#
# Ex: If the input is:    45
#     the output is:      1 quarter
#                         2 dimes
#
# Your program must define and call the following function.
# The function exact_change() should return num_dollars,
# num_quarters, num_dimes, num_nickels, and num_pennies.
# def exact_change(user_total)
#
##################################################################

# Define your function here

if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Type your code here.
