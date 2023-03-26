#    Mad Libs are activities that have a person provide various words,
#    which are then used to complete a short story in unexpected (and
#    hopefully funny) ways.
#
#    Write a program that takes a string and an integer as input,
#    and outputs a sentence using the input values as shown in the
#    example below. The program repeats until the input string is
#    quit and disregards the integer input that follows.
#
#    Ex:
#    If the input is:
#    apples 5
#    shoes 2
#    quit 0
#
#    the output is:
#    Eating 5 apples a day keeps the doctor away.
#    Eating 2 shoes a day keeps the doctor away.

###################################################################################

# while True, continue to assign user input to user_input to create Mad Libs
while True:
    user_input = input()

    # in case user does not enter enough words/numbers use a 'try' block to handle any ValueErrors
    try:
        # split user_input into 'word' and 'number' variables
        word, number = user_input.split()
    except ValueError:  # raise ValueError, continue loop
        continue

        # Check for quit using an 'if' statement, break if True
    if word == 'quit':
        break
    # if word == 'quit' is False
    else:
        print(f"Eating {number} {word} a day keeps the doctor away.")

####################################################################
## RESULT: 100
