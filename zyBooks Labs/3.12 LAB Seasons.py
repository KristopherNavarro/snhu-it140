# 3.12 LAB: Seasons
# Write a program that takes a date as input and outputs
# the date's season. The input is a string to represent
# the month and an int to represent the day.
#
#   Ex:     If the input is:    April
#                               11
#           the output is:      Spring
#
# In addition, check if the string and int
# are valid (an actual month and day).
#
#   Ex:     If the input is:    Blue
#                               65
#           the output is:      Invalid
#
# The dates for each season are:
#   Spring:  March 20   -   June 20
#   Summer:  June 21    -   September 21
#   Autumn:  September 22 - December 20
#   Winter:  December 21 -  March 19

# import the sys package for exit() method
# import pandas for date range handling
import sys
import pandas as pd

# retrieve two inputs from user, first is month in string form, second is day number
input_month = input()
input_day = int(input())

# Create a dictionary to converting alpha month names to numeric
month_nums = {'January': 1,'February': 2,'March': 3,'April': 4,'May': 5,'June': 6,'July': 7,\
              'August': 8,'September': 9,'October': 10,'November': 11,'December': 12}

# create a function for handling invalid months, print 'invalid' if the user supplied month
# is not a valid month in the month_nums dict.
def month_conversion(month):
    try:    # if key is present, return the alpha for the month supplied by user
        month_number = str(month_nums[month])
        return month_number
    except KeyError:    # if key is not present, print 'invalid' and end program.
        print('Invalid')
        sys.exit()

# Create a function that creates date_range objects from two user inputs,
# a start date in Month and day ('MM-DD'), an end date in the same format,
# and returns a DataFrame object.
def date_ranges(start_MM_DD, end_MM_DD):
    start = '2000-' + str(start_MM_DD)  # concat a generic year before the supplied start date
    end = '2000-' + str(end_MM_DD)      # same for the end date
    df_range = pd.DataFrame(pd.date_range(start=start,end=end)) # df created from a date_range object
    return df_range

# Create a function for querying the date_range dataframes
def check(dataframe, season):       # takes two arguments: the dataframe to check and the season to print
    for index, row in dataframe.iterrows():
        if (row == user_date).bool():   # use the .bool() method on df to avoid errors
            print(season)
            sys.exit()      # if match is found, program terminates
        else:
            pass


# use the date_ranges function to create individual dataframes for each season
spring = date_ranges('03-20', '06-20')
summer = date_ranges('06-21', '09-21')
autumn = date_ranges('09-22', '12-20')
winter = date_ranges('12-21', '12-31').append(date_ranges('01-01','03-19'))     # append two ranges, winter overlaps years
## NOTE: Although pd.append() is deprecated, I am using it here for simplicity and time saving
# - all other joining methods were giving me trouble and I'm running out of time to submit.

# Reassignments: input_month using month_conversion, input_day using str()
input_month = month_conversion(input_month)
input_day = str(input_day)
user_date = f'2000-{input_month}-{input_day}'   # concats the format required to query the date_range dataframes

# Call check() on each of the season dataframes along with passing the name of the string to print if True.
check(spring,'Spring')
check(summer,'Summer')
check(autumn,'Autumn')
check(winter,'Winter')

# If none of the check() functions return a match, print 'Invalid'
print('Invalid')

#######################################################################################################3
## RESULT: PASS 10/10


