# Give the two strings as user input using the input() function
# and store them in two separate variables.
firststrng = input('Enter some random first string = ')
secondstrng = input('Enter some random second string = ')
# Take a variable to say stringLength1 that stores the length of the given first string.
# Initialize the stringLength1 to 0.
stringLength1 = 0
# Take a variable to say stringLength2 that stores the length of the given second string.
# Initialize the stringLength2 to 0.
stringLength2 = 0
# Using for loop to traverse over the elements of the first string.
for charact in firststrng:
    # Increment the stringLength1 (Count Variable) by 1.
    stringLength1 = stringLength1+1
# Using for loop to traverse over the elements of the second string.
for charact in secondstrng:
    # Increment the stringLength2 (Count Variable) by 1.
    stringLength2 = stringLength2+1
# Compare the count variables(stringLength1 ,stringLength2) of both
# the strings using if conditional statement.
# If the stringlength1 is greater than stringlength2 then
# print the first string using the print() function.
if(stringLength1 > stringLength2):
    print('The string', firststrng, 'is larger string')
# If the stringlength1 is equal to stringlength2 then
# print both the strings are equal using the print() function.
elif(stringLength1 == stringLength2):
    print('The strings', firststrng, 'and', secondstrng, 'are equal in size')
# If the stringlength1 is less than stringlength2 then
# print the second string using the print() function.
else:
    print('The string', secondstrng, 'is larger string', firststrng)