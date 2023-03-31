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

def exact_change(user_total):

    # perform floor division on 'user_total', divide by 100, assign to 'dollars'
    # assign 'remainder' to 'user_total' minus 'dollars' times 100
    dollars = user_total // 100
    remainder = user_total - (dollars * 100)

    # perform floor division on 'remainder', divide by 25, assign to 'quarters'
    # assign 'remainder' to 'remainder' minus 'quarters' times 25
    quarters = remainder // 25
    remainder = remainder - (quarters * 25)

    # perform floor division on 'remainder', divide by 10, assign to 'dimes'
    # assign 'remainder' to 'remainder' minus 'dimes' times 10
    dimes = remainder // 10
    remainder = remainder - (dimes * 10)

    # perform floor division on 'remainder', divide by 10, assign to 'nickels'
    # assign 'remainder' to 'remainder' minus 'nickels' times 10
    nickels = remainder // 5
    remainder = remainder - (nickels * 5)

    # perform floor division on 'remainder', divide by 5, assign to 'pennies'
    pennies = remainder // 1


    # Create a global dict with keys being the denomination in singular form and the values being the equivalent variable.
    #   ex. {'dollar':dollars}
    global denominations
    denominations = {'dollar':dollars, 'quarter':quarters, 'dime':dimes, 'nickel':nickels, 'penny':pennies}

    # return only the values of the denomination dict
    num_dollars = denominations['dollar']
    num_quarters = denominations['quarter']
    num_dimes   = denominations['dime']
    num_nickels = denominations['nickel']
    num_pennies = denominations['penny']

    return (num_dollars,num_quarters,num_dimes,num_nickels,num_pennies)

if __name__ == '__main__':
    input_val = int(input())
    # denomination values are assigned to individual variables
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Create copy of the denominations dict named 'change'
    change = denominations.copy()

    # if statement to handle the variability of the print statements (singular / plural)
    # Start by printing 'No change' if 'amount' equals 0
    if input_val == 0:
        print('no change')
    else:  # start a for loop to handle singular / plural printing
        for k, v in change.items():  # parse through each key and value of the denominations dict
            if v == 1:  # if the value is 1, print the value and key
                print(v, k)
            elif v == 0:  # for values that are zero, skip printing
                continue
            else:
                if k != 'penny':  # if the key is not penny, then simple print the value, key and concat 's' to key
                    print(v, k + 's')
                else:
                    print(v,
                          'pennies')  # if the 'pennies' variable is greater than 1, print 'pennies' instead of 'pennys'

##################################################################################
# GRADE: 10/10