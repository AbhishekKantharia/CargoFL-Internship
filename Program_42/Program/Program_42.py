# Give the string as user input using the input() function and store it in a variable.
gvn_str = input("Enter some random string = ")
# Take a new empty string say 'new_str'and store it in another variable.
new_str = ""
# Loop in the above-given string using the for loop.
for itror in gvn_str:
    # Get the ASCII value of the iterator using the ord() function and store it in
    # another variable say 'numb'.
    numb = ord(itror)
 # Check if the above-obtained number is greater than or equal to '0' using the
# if conditional statement.
    if (numb >= 0):
        # If the statement is true, check again if the given number is less than or equal to '127'
        # using the if conditional statement.
        if (numb <= 127):
            # If the statement is true, then concat the 'new_str' with the iterator value and
            # store it in the same variable new_str'.
            new_str = new_str + itror
# Print the above-given string after removal of any Non-ASCII Characters.
print("The given string after removal of any Non-ASCII Characters = ", new_str)