# Give the first string as user input using input() function and store it in a variable.
fst_str = input("Enter some random string = ")
# Give the second string as user input using input() function and store it in another variable.
secnd_str = input("Enter some random string = ")
# Check if the length of the first string is not equal to the length of the second
# string using the if conditional statement and using the len() function.
if(len(fst_str) != len(secnd_str)):
    # If the statement is true, print "The given second string is not the rotation of the given first string".
    print("The given second string is not the rotation of the given first string")
else:
    # Else concat the first string with the first string itself using the '+ ' operator
    # and store it in a variable say "conat_str".
    conct_str = fst_str + fst_str
# Check if the second string is present in the "conca_str" using the if
# conditional statement.
    if(secnd_str in conct_str):
        # If the statement is true, print  "The given second string is the rotation of the given first string".
        print("The given second string is the rotation of the given first string")
    else:
        # Else print  "The given second string is not the rotation of the given first string".
        print("The given second string is not the rotation of the given first string")