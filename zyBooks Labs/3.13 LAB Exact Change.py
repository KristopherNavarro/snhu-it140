#  Write a program with total change amount as an integer input, and output
#  the change using the fewest coins, one coin type per line. The coin types
#  are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural
#  coin names as appropriate, like 1 Penny vs. 2 Pennies.
#
#   Ex:     If the input is:    0 (or less than 0),
#           the output is:      No change
#
#   Ex:     If the input is:    45
#           the output is:      1 Quarter
#                               2 Dimes

# Take a user input() passed to int(), assign to 'amount'
amount = int(input())

# perform floor division on 'amount', divide by 100, assign to 'dollars'
# assign 'remainder' to 'amount' minus 'dollars' times 100
dollars = amount // 100
remainder = amount - (dollars * 100)

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


# Create a dict with keys being the denomination in singular form and the values being the equivalent variable.
#   ex. {'dollar':dollars}
denominations = {'Dollar':dollars, 'Quarter':quarters, 'Dime':dimes, 'Nickel':nickels, 'Penny':pennies}

# if statement to handle the variability of the print statements (singular / plural)
# Start by printing 'No change' if 'amount' equals 0
if amount == 0:
    print('No change')
else:   # start a for loop to handle singular / plural printing
    for k,v in denominations.items():   # parse through each key and value of the denominations dict
        if v == 1:  # if the value is 1, print the value and key
            print(v, k)
        elif v == 0:    # for values that are zero, skip printing
            continue
        else:
            if k != 'penny':    # if the key is not penny, then simple print the value, key and concat 's' to key
                print(v, k + 's')
            else:
                print(v, 'Pennies') # if the 'pennies' variable is greater than 1, print 'pennies' instead of 'pennys'

#########################################################
# RESULT: PASS 10/10