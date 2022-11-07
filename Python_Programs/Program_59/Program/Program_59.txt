# Import math module using the import keyword.
import math
# Give the string as user input using the input() function and 
# store it in a variable.
gven_str = input("Enter some random String = ")
# Take a variable to say lexicogrpc_rank and initialize its value to 1.
lexicogrpc_rank = 1
# Calculate the length of the given string using the len() function and decrease it by 1.
# Store it in another variable say str_lengt.
str_lengt = len(gven_str)-1
# Loop from 0 to the above length using the for loop.
for itr in range(0, str_lengt):
    # Inside the loop, take a variable to say cnt and initialize its value to 0.
    cnt = 0
    # Loop from the itr+1 to the above str_lengt (where itr is the iterator value of the parent
    # for loop) using the for loop.
    for k in range(itr+1, str_lengt+1):
      # Inside the loop, check if the character present at the iterator value of the parent for
      # loop is greater than the character present at the iterator value of the inner for
      # loop using the if conditional statement.
        if gven_str[itr] > gven_str[k]:
         # If the statement is true, then increment the value of the above-initialized cnt by 1.

            cnt += 1
    # Calculate the factorial of (str_lengt - itr) using the math.factorial() function and
    # store it in another variable. (where itr is the iterator value of the parent for loop)
    f = math.factorial(str_lengt-itr)
    # Multiply the above result with cnt and add the result to the lexicogrpc_rank.
    # Store it in the same variable lexicogrpc_rank.
    lexicogrpc_rank += cnt*f
# Print the lexicogrpc_rank to get the Lexicographic Rank of a given string.
print("The given String's {", gven_str,
      "} Lexicographic Rank = ", lexicogrpc_rank)