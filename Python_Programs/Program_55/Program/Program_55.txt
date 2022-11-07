# Create a recursive function say numberof_ways() which accepts the given number
# as an argument and returns the total number of ways friends can get to the party.


def numberof_ways(no_frnds):
    # Inside the function, check if the given number is less than 3 using the if
        # conditional statement.
    if(no_frnds < 3):
        # If it is true, then return the given number.
        return no_frnds
    # Return the value of count_no_ways(no_frnds-1)) + ((no_frnds-1) *
        # count_no_ways(no_frnds-2) (Recursive Logic).
    return (numberof_ways(no_frnds-1)) + ((no_frnds-1) * numberof_ways(no_frnds-2))


# Give the number(no of friends) as user input using the int(input()) function and store it in a variable.
no_frnds = int(input("Enter some random number = "))
# Pass the given number as an argument to the numberof_ways() function and
# store it in a variable.
rslt = numberof_ways(no_frnds)
# Print the above result.
print("Different ways the", no_frnds, "friends can get to the party = ", rslt)