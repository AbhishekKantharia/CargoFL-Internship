# Function to remove adjacent duplicates characters from a string
def remAdj(givenstrng):
    # convert the given string to list using list() function
    charslist = list(givenstrng)
    prevele = None
    p = 0
    # Traverse the given string
    for chars in givenstrng:
        if prevele != chars:
            charslist[p] = chars
            prevele = chars
            p = p + 1
    # join the list which contains characters to string using join function and return it
    return ''.join(charslist[:p])


# Driver code
# Give the string as user input using the input() function.
# Store it in a variable.
givenstrng = input('Enter some random string = ')
# printing the given string before removing adjacent duplicate characters
print('given string before removing adjacent duplicate characters = ', givenstrng)
# Pass the given string to the remAdj function which accepts
# the given string as the argument
# and returns the modified string with no adjacent duplicates.
modistring = remAdj(givenstrng)
# printing the given string after removing adjacent duplicate characters
print('given string without after adjacent duplicate characters = ', modistring)