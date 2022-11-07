# Create a function listchunks() that accept the given list
# and the number as arguments and return the chunks of the given list.


def listchunks(gvnlst, gvnumb):
        # Calculate the length of a list using the len() function.
    lstleng = len(gvnlst)
    # Inside the function iterate from 0 to the length of the
    # given list and give the third parameter as n in the range() function
    # using the For loop.
    for m in range(0, lstleng, gvnumb):
        # Using the yield keyword slice from iterator value to the length of the list.
        yield gvnlst[m:m + gvnumb]


# Give the list as user input using the list(), input() functions,
# and store the list in a variable.
gvnlist = list(
    input('Enter some random string elements for the list = ').split())
# Give the Number N as user input using the int(input()) function
# and store it in another Variable.
numb = int(input('Enter some random number = '))
# Pass the given list and number N to listchunks() function.
resllt = listchunks(gvnlist, numb)
# Convert this result to the list() and store it in a variable.
resllt = list(resllt)
# Print the above result.
print(resllt)