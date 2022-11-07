# function which prints the permutations
def printPermutations(string, start, end):
    i = 0
    # printing the permutations
    if(start == end-1):
        print(string)
    else:
        for i in range(start, end):

           # Fixing a character and swapping the string
            samstring = list(string)
            # swapping using ,
            samstring[start], samstring[i] = samstring[i], samstring[start]
      # For the remaining characters, call printPermutations() recursively.

            printPermutations("".join(samstring), start+1, end)
            # Fixing a character and swapping the string
            # swapping using ,
            samstring[start], samstring[i] = samstring[i], samstring[start]


# given string
string = "cold"
# calculating the length of string
length = len(string)
print("Printing all permutations of the given string", string)
# passing string and 0th index as it is fixed at the starting
printPermutations(string, 0, length)