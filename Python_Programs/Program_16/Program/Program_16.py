# Function to find the majority element present in a given list
def majoElement(given_list):
    # majo stores the majority element (if present in the given list)
    majo = -1
    # initializing counter index with 0
    ind = 0
    # do for each element `A[j]` in the list
    for j in range(len(given_list)):
        # check if the counter index is zero or not.
        if ind == 0:
            # set the current candidate of the given list to givenlist[j]
            majo = given_list[j]
            # change the counter index to 1.
            ind = 1
        # Otherwise, if givenlist[j] is a current candidate, increment the counter.
        elif majo == given_list[j]:
            ind = ind + 1
        # Otherwise, if givenlist[j] is a current candidate, decrement the counter.
        else:
            ind = ind - 1
    # return the majority element
    return majo

# Driver Code
# Give the list as static input and store it in a variable.
given_list = [4, 11, 13, 9, 11, 11, 11, 3, 15, 28, 11, 11, 11, 11]
# Pass the given list to the majoElement function which accepts
# the given list as an argument
# and implement the Boyer–Moore majority vote algorithm.

print("The majority element present in the givenlist",given_list, '=', majoElement(given_list))