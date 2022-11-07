# Give the two numbers m and n as user input using map(), int(), and split() functions.
# Store them in two separate variables.
mNumb, nNumb = map(int, input('Enter some random numbers M and N =').split())
# Take a variable result and initialize the variable with 0.
resu = 0
# Loop till M is greater than N using while loop.
while(mNumb > nNumb):
    # Check if M is even or odd using the If statement.
    if (mNumb & 1):
        # If it is true then increment the value of M by 1 and result by 1.
        mNumb += 1
        resu += 1
    # Divide the M by 2 after the end of the If statement.
    mNumb //= 2
    # Increment the result by 1.
    resu += 1
# Print the result +N-M.
resu = resu+nNumb-mNumb
print('The result is', resu)