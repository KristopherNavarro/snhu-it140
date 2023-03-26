# Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

# i becomes !
# a becomes @
# m becomes M
# B becomes 8
# o becomes .
# Ex: If the input is: mypassword
# the output is:       Myp@ssw.rdq*s

# Hint: Python strings are immutable, but support string concatenation. Store and build the stronger password in the given password variable.

###########################################

word = input()
password = ''

# create dict containing characters to be replaced as keys, and the replacement char as the value
replacements = {'i':'!', 'a':'@', 'm':'M', 'B':'8', 'o':'.'}

# iterate over characters in 'word' using for  loop
for ch in word:
	# check if character is present in replacements.keys()
	if ch in replacements.keys():
		password += replacements[ch] # if True, add the corresponding value to 'password'
	else:
		password += ch # if False, add the character to 'password'

# concat 'q*s' to the end of 'password'
password += 'q*s'

# print the final password
print(password)

##################################################################3
## RESULT: 100
