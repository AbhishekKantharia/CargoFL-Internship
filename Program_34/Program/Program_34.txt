# Give the string as user input using the input() function and store it in a variable.
given_strng = input('Enter some random string = ')
# Take a variable to say stringcharacters that stores the total characters in the given string.
# Initialize the stringcharacters to 0.
stringcharacters = 0
# Traverse the given string using for loop.
for charact in given_strng:
    # Increment the value of stringcharacters by 1.
    stringcharacters = stringcharacters+1
# Using String Concatenation and slicing form the new string with which is made of the First two
# and Last two characters From a Given String.
resstring = given_strng[0:2]+given_strng[stringcharacters-2:stringcharacters]
# print the result string
print(resstring)