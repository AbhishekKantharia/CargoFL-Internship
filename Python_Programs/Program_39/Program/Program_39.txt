# Give the string as user input using the input() function and store it in a variable.
gvn_str = input("Enter some random string = ")
# Take a new empty string say 'new_str'and store it in another variable.
new_str = ""
# Take a variable and initialize its value with '0' and store it in another variable.
itr = 0
# Loop from '0' to the length of the given string -1 using for loop and len() function.
for itr in range(0, len(gvn_str)-1):
    # Concat the new_str with the iterator value of the given string and
    # store it in the same variable 'new_str'
    new_str = new_str + gvn_str[itr]
# Check if the iterator value of the given input string is equal to the iterator+1 value
# of the given input string using the if conditional statement.
    if(gvn_str[itr] == gvn_str[itr+1]):
      # If the statement is true, concat the 'new_str' with the '*' symbol and
      # store it in the same variable 'new_str'.
        new_str += '*'
# Print the variable 'new_str' to enter '*' between two identical characters in a
# given String.
print("The given string after entering '*' between two identical characters=", new_str)