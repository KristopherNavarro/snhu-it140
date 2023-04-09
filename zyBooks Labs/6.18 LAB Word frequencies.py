# Write a program that reads a list of words. Then, the
# program outputs those words and their frequencies.
#
# Ex:   If the input is:    hey hi Mark hi mark
#       the output is:      hey 1
#                           hi 2
#                           Mark 1
#                           hi 2
#                           mark 1
#
########################################################

# take user input assigned to user_input
user_input = 'hey hi Mark hi mark'

# split user_input into tokens list
tokens = user_input.split()

# initiate token_dict for storing pairs of tokens as keys and number of occurrences as values
token_dict = {}

# Loop over tokens adding each item as a key in tokens_dict
for token in tokens:
    token_dict[token] = 0
    #loop over tokens.copy() to count the number of occurrences of each token
    for t in tokens.copy():
        # if there is a match, increment corresponding value in token_dict
        if token == t:
            token_dict[token] += 1

# to match the required output, iterate over the tokens list
for token in tokens:
    # then iterate over tokens_dict
    for k, v in token_dict.items():
        # print the corresponding key and value combinations for each token
        if token == k:
            print(k, v)

####################################################################################
# RESULT: 10/10