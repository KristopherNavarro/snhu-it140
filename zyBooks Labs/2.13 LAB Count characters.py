# Write a program whose input is a string which contains a character
# and a phrase, and whose output indicates the number of times the
# character appears in the phrase.

#  Ex:  If the input is:    n Monday
#       the output is:      1
#  Ex:  If the input is:    z Today is Monday
#       the output is:      0
#  Ex:  If the input is:    n It's a sunny day
#       the output is:      2
#               Case matters.
#  Ex:  If the input is:    n Nobody
#       the output is:      0
#               n is different than N.

user_string = input()

char_to_find = user_string[0]
num_instances = user_string.count(char_to_find,1)
print(num_instances)