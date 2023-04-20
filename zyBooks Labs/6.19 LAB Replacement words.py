# Write a program that replaces words in a sentence. The input begins with
# word replacement pairs (original and replacement). The next line of input
# is the sentence where any word on the original list is replaced.
#
# Ex:   If the input is:    automobile car   manufacturer maker   children kids
#                               The automobile manufacturer recommends car seats for children
#                               if the automobile doesn't already have one.
#       the output is:      The car maker recommends car seats for kids if the car doesn't already have one.
#
# You can assume the original words are unique.
#
##############################################################################################

# Take first input with word and replacement
user_input = input()

# split into pairs
pairs = user_input.split('   ')

# Dictionary for holding words and replacements
replacement_dict = {}

# loop over pairs, splitting then assigning the first item as a key
# and second item as a corresponding value in replacement_dict
for pair in pairs:
    var = pair.split()
    replacement_dict[var[0]] = var[1]

# Take second user input
user_input2 = input()

# Split second input into a list for easy replacement
sentence = user_input2.split()

# Empty string for concatenating the final sentence
replacement_sentence = ''

# Loop over words in second sentence, replacing with values from
# replacement_dict where available
for word in sentence:
    # Words not in replacement_dict will raise KeyErrors
    # use try block to handle KeyErrors
    try:
        # add replacement words from replacement_dict to replacement_sentence with whitespace
        replacement_sentence += replacement_dict[word] + ' '
    except KeyError:
        # add original word to replacement_sentence with whitespace
        replacement_sentence += word + ' '

# Print the final replacement sentence, strip any whitespace from the end of the sentence
print(replacement_sentence.rstrip())

##########################################################################################
# RESULT: 10/10
