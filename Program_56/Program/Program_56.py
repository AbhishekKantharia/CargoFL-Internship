# Create a function checkAp() which returns true if the given list
# is in Arithmetic Progression Else it returns False.


def checkAp(gvnlst):
  # Calculate the length of the given list using the length() function.
    lstlen = len(gvnlst)
    # Inside the Function sort the given list using the built-in sort() function.
    gvnlst.sort()
    # Now compute the difference between the first two elements of the given list and
    # initialize a new variable commondif with this difference.
    commondif = gvnlst[1]-gvnlst[0]
    # Traverse the array in reverse order i.e from n-1 to 1 index using For loop.
    for m in range(lstlen-1, 1, -1):
      # Compare the difference between successive elements.

        if(gvnlst[m]-gvnlst[m-1] != commondif):
          # If the difference is not equal to commondif then return False.
            return 0
    # After the end of For loop return True (This signifies that the given list is in Ap)
    return 1


# Give the list as user input using list(),map(),input(),and split() functions.
# store it in a variable.
givenlist = list(
    map(int, input('Enter some random List Elements separated by spaces = ').split()))
# Pass the given list as an argument to the checkAp() function.
if(checkAp(givenlist)):
    print('The given list', givenlist, 'is in AP')
else:
    print('The given list', givenlist, 'is not in AP')