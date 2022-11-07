def findKadane(givnList, listleng):
    # Set both of the variablesto the value at the first index, i.e., givnList[0].
    cur_maxi = givnList[0]
    maxi_so_far = givnList[0]

    for i in range(1, listleng):
      # Store the maximum of givnList[i] and cur_maxi + givnList[i]
      # in the cur_maxi for the following index i.
        cur_maxi = max(givnList[i], cur_maxi + givnList[i])
        # maxi_so_far stores the maximum of maxi_so_far and cur_maxi.
        maxi_so_far = max(maxi_so_far, cur_maxi)
    # return the maxi_so_far
    return maxi_so_far


# Give the array/list as static input and store it in a variable.
givnList = [-3, 4, 1, 2, -1, -4, 3]
# Calculate the length of the given list
# using the len() function and store it in a variable.
listleng = len(givnList)
# Pass the given list and length of the given
# list as an arguments to the findKadane function which implements the kadane's algorithm.
resltsum = findKadane(givnList, listleng)
# Print the maximum sum.
print('The maximum subarray sum of the given list', givnList, ':')
print(resltsum)