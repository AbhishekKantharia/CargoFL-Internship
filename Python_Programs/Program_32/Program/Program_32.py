# Give the string as user input using input() function and store it in a variable.
given_string = input('Enter some random string =')
# Take a variable to say stringchars that store the total characters in the given string.
# Initialize the stringchars to 0.
stringchars = 0
# Take a variable to say stringwords that stores the total words in the given string.
# Initialize the stringwords to 1.
stringwords = 1
# To traverse the characters in the string, use a For loop.
for charact in given_string:
   # If a space character is encountered then increment the stringwords by 1.
    if(charact == ' '):
        stringwords = stringwords+1
     # increment the stringchars variable each time by 1.
    stringchars = stringchars+1
# Print the stringLength.
print(
    'Total characters present in given string {', given_string, '} =', stringchars)
print(
    'Total words present in given string {', given_string, '} =', stringwords)
