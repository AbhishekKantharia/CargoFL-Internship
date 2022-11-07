# Import re(regex) module using the import keyword
import re
# Give some random mobile number as user input using the input() 
# function and store it in a variable.
gvn_mobilenumb = input("Enter some random mobile number = ")
# Pass the Pattern, given mobile number as arguments to the fullmatch() function to 
# check if the entire mobile number matches the pattern else it returns None.
# Store it in a variable
# Here the pattern represents that the starting number should be between 6-9
# and the next nine digits can be any number between 0 and 9.
rslt = re.fullmatch('[6-9][0-9]{9}',gvn_mobilenumb) 
# Check if the above result is not Equal to None Using the if conditional statement
if rslt!=None: 
     # If it is true, i.e the output is not None then print "Valid Number"
     print('The given mobile number is a Valid Number')
else:
     # Else print "Invalid Number"
     print('The given mobile number is Invalid')