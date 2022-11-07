def countSetBit(numb):
    # checking if the given number is greater than 1
    if numb > 1:
      # Set the variable say setbitcount to 0 to count the total number of set bits.
        setbitcount = 0
        # looping till number greater than 0 using while loop
        while(numb > 0):
            numb = numb & (numb-1)
            # increment the set bit count
            setbitcount = setbitcount+1
    # return the setbitcount
    return setbitcount


# Driver code
given_numb = 4322
# passing given number to countSetBit function to
# count the total number of set bits in the given number
print("The total number of set bits in the given number ", given_numb, " : ")
print(countSetBit(given_numb))