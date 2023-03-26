#This program will output a right triangle based on user specified height triangle_height and symbol triangle_char.

#(1) The given program outputs a fixed-height triangle using a * character. Modify the given program to output a
# right triangle that instead uses the user-specified triangle_char character. (1 pt)

#(2) Modify the program to use a loop to output a right triangle of height triangle_height. The first line will
# have one user-specified character, such as % or *. Each subsequent line will have one additional user-specified
# character until the number in the triangle's base reaches triangle_height. Output a space after each user-specified
# character, including a line's last user-specified character. (2 pts)

#Example output for triangle_char = % and triangle_height = 5:

#Enter a character:      %
#Enter triangle height:  5

# % 
# % % 
# % % % 
# % % % % 
# % % % % % 

##################################################################################################

# assign user input for character to triangle_char
# assign user input for height to triangle_height assigned to triangle_height, passed as an int()
triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

# Iterate through a range from 0 to triangle_height inclusive, using a for loop
# for each iteration, print the product of the interative and triangle_char plus whitespace
for i in range(triangle_height+1):
    print((triangle_char + " ") * i)

###############################################################3
## RESULT: 100