# Give string and substring as user input using input() function
# and store them in two separate variables.
given_strng = input('Enter some random string = ')
# given substring
given_substring = input('Enter some random substring = ')
# Using the in-built find() method, determine
# whether the substring exists in the given string.
# If the find() function returns -1 then the given substring isn't found in the given string.
if(given_strng.find(given_substring) == -1):
    print('The substring [', given_substring,'] is not found in [', given_strng, ']')
else:
    print('The substring [', given_substring,'] is found in [', given_strng, ']')