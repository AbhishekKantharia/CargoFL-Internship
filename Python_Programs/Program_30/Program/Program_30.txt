# Take a function that swaps the first and last character of the string.
def swapString(given_string):
    # Split the string in the function.
    # The last character is then added to the middle half of the string,
    # which is then added to the first character.
    modifiedstring = given_string[-1:] + given_string[1:-1] + given_string[:1]
    # The modified string will be returned.
    return modifiedstring


# Give the string as user input using int(input()) and store it in a variable.
given_string = input('Enter some random string = ')
# printing the original string before modification
print('The original string before modification =', given_string)
# Pass the given string as an argument to the function.
modified_string = swapString(given_string)
# printing the new string after modification
print('The new string after modification =', modified_string)