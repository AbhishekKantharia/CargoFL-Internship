# Give the string as User input and store it in a variable.
gvn_strng = input("Enter Some Random String = ")
# Initialize two empty stings
fst_strng, secnd_strng = '', ''
# If the length of the Given String is even ,then divide it into two equal halves
# using slicing operator and append it to the above two declared empty strings.
if(len(gvn_strng) % 2 == 0):
    fst_strng = gvn_strng[:len(gvn_strng)//2]
    secnd_strng = gvn_strng[len(gvn_strng)//2:]
# Else if the length of the Given String is odd ,then divide it into two equal halves
# using slicing operator(Ignore middle character ) and append it to the above two declared empty strings.
else:
    fst_strng = gvn_strng[:len(gvn_strng)//2]
    secnd_strng = gvn_strng[len(gvn_strng)//2+1:]
# Convert the split strings S1, S2 into two lists respectively using built-in list()
# function and store them in another variables.
lst_1 = list(fst_strng)
lst_2 = list(secnd_strng)
# Sort the above two lists in ascending order and store them in another variables .
lst_1.sort()
lst_2.sort()
# Convert the above two lists into two different strings respectively and
# store them in another variables .
fst_strng = str(lst_1)
secnd_strng = str(lst_2)
# If both the given split strings are equal ,print "Lapindrome " using if condition.
if(fst_strng == secnd_strng):
    print('Yes, the above Given string is a lapindrome')
# print "Not Lapindrome", if both the given split strings  are not equal .
else:
    print('No, the above given string is not a lapindrome')