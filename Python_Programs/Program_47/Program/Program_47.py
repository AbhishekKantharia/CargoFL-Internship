# Take a dictionary and initialize it to empty
# using the {} or dict() say freqncyDictionary.
freqncyDictionary = {}
# Give the string as the user input using the input() function and store it in a variable.
gvnstrng = input("Enter some random string = ")
# Loop in the given string using the For loop.
for i in gvnstrng:
        # Inside the For loop,
    # Check if the string character is present in the dictionary
    # or not using the if conditional statement and 'in' keyword.
    if i in freqncyDictionary.keys():
                # If it is true then increment the count of the string character
        # in the dictionary by 1.
        freqncyDictionary[i] = freqncyDictionary[i]+1
    # Else initialize the dictionary with the string character as key and value as 1.
    else:
        freqncyDictionary[i] = 1
# Give the k value as user input using the int(input()) function and store it in a variable.
k = int(input("Enter some random number = "))
# Take a string which stores all the characters which are not occuring even number
# of times and initialize it to null string using "" or str()
modifd_string = ""
# loop in the given string using the for loop
for charac in gvnstrng:

        # check if the character has frequency greater than or equal to k by checking value of that character in frequency dictionary
        # we check using the if conditional statement
    if(freqncyDictionary[charac] >= k):
        # if it is true then concatenate this character to modifd_string using string concatenation
        modifd_string = modifd_string+charac

# print the modifd_string string
print('The given string {', gvnstrng,'} after removal of all characters that appears more than {', k, '} times :', modifd_string)