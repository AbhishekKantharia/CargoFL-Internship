# Take a variable(say secpassword) and create some random characters as tuple
# (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'), ('I', '|')).
secpassword = (('s', '$'), ('and', '&'),
               ('a', '@'), ('o', '0'), ('i', '1'),
               ('I', '|'))
# Create a function createSecurePassword() which accepts the given password
# as an argument and returns the secure password.


def createSecurePassword(givenpassword):
    # Loop using two variables in the secpassword using For loop.
    for m, n in secpassword:
      # Replace the password with the two variables.
        givenpassword = givenpassword.replace(m, n)
    # Return the modified Password.
    return givenpassword


# Give the password as user input using the input() function and store it in a variable.
givenpassword = input('Enter some random password = ')
print('The original Password = ', givenpassword)
# Pass the given password as an argument to createSecurePassword() function.
modifiedpassword = createSecurePassword(givenpassword)
# Print the New Modified Password.

print('The new modified password = ', modifiedpassword)