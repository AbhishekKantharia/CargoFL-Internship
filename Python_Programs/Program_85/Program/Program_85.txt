# function which return index if element is present else return -1
def sentinelSearch(given_list, key):
    # getting the last element of the list
    lastelement = given_list[-1]

    # the key which should  be searched is kept at the end of the last index.
    given_list[-1] = key
    i = 0

    while (given_list[i] != key):
        i += 1

    # Put the last element back
    given_list[-1] = lastelement
    # getting length of list
    length = len(given_list)
    if ((i < length - 1) or (given_list[length - 1] == key)):
        return i
    else:
        return -1


# given_list
given_list = [2, 7, 3, 4, 9, 15]

# given key
key = 9
# passing the given_list and key to sentinelSearch function
res = sentinelSearch(given_list, key)
# if result is equal to -1 then element is not present in list
if(res == -1):
    print("Given element(key) is not found in list")
else:
    print("Element", key, "is found at index", res)