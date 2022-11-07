# Give the string as user input using int(input()) function and store it in a variable.
given_string = input('Enter some random string = ')
# printing the original string before modification
print('The original string before modification =', given_string)
# Using the replace function replace all blank space with a hyphen by providing blank space as the first argument
# and hyphen as the second argument in replace function.
modified_string = given_string.replace(' ', '-')
# printing the new string after modification
print('The new string after modification =', modified_string)