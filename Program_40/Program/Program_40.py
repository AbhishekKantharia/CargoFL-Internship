# Give the string as User input  using the input() function and store it in a variable.
gvn_strng = input("Enter some Random String = ")
# Print the above given string .
print("The above given string = " + str(gvn_strng))
# Give the number of trailing zeros to be added as User input using the int(input()) function and store it in another
# variable.
No_trzers = int(input("Enter some Random Number = "))
# Calculate the length of the above given string using built- in len() function .
# Add it with the given number of zeros and store it in another variable.
tot_lenth = No_trzers + len(gvn_strng)
# Add the given number of trailing zeros to the above given String Using built-in ljust()
# method and store it in another variable.
finl_reslt = gvn_strng.ljust(tot_lenth, '0')
# Print the above Given string with added given number of trailing Zeros.
print("The above Given string with added given number of trailing zeros = ", finl_reslt)