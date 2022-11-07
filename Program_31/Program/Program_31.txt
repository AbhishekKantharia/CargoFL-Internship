# function  that accepts the string as an argument
# and removes all the characters present at odd indices in the given string.


def removeOddString(givenstrng):
    # In the function take an empty string say tempstng using '' .
    tempstng = ""
    # Traverse the given string using For loop.
    for charindex in range(len(givenstrng)):
        # Use an if statement and modulus operator to
        # determine whether the string's index is odd or even.
        if charindex % 2 == 0:
            # If the index is an even number, append the
            # character to the tempstng using String Concatenation.
            tempstng = tempstng + givenstrng[charindex]
    # Return the tempstng.
    return tempstng


# Give the string as the user input with the help of input() function and store it in a variable.
givenstrng = input('Enter the given random string = ')
# print the given string without modification'
print('The given string before modification = ', givenstrng)
# Pass the given string as an argument to the removeOddString function.
resstrng = removeOddString(givenstrng)
# print the given string after modification
print('The given string after modification = ', resstrng)