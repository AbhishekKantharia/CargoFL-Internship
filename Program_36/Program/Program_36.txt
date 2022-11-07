# Import keyword module using import keyword.
import keyword
# Get all the keywords in python using keyword.kwlist method and store it in a variable.
keywrds_lst = keyword.kwlist
# Give the first string as user input using the input() function and
# store it in another variable.
fst_str = input("Enter some random string = ")
# Give the second string as user input using the input() function and
# store it another variable.
secnd_str = input("Enter some random string = ")
# Check whether the given first string is present in the above keyword list or not
# using if conditional statement.
if fst_str in keywrds_lst:
  # If the given condition is True , print "keyword".
    print("The given string{", fst_str, "} is a keyword")
else:
  # If the given condition is False , print " Not keyword" using else conditional statement.
    print("The given string{", fst_str, "} is not a keyword")
# Check whether the given second string is present in the above keyword or not list
# using if conditional statement.
if secnd_str in keywrds_lst:
  # If the given condition is True , print "keyword".
    print("The given string{", secnd_str, "} is a keyword")
else:
  # If the given condition is False , print " Not keyword" using else conditional statement.
    print("The given string{", secnd_str, "} is not a keyword")