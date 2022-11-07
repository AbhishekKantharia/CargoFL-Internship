# Give the string as user input using the input() function and store it in a variable.
gvn_str = input("Enter some random string = ")
# Give the number say 'n' as user input using int(input()) and store it in another variable.
num = int(input("Enter some random number = "))
# Calculate the len of the given string using the len() function and store it
# in another variable.
len_str = len(gvn_str)
#Divide the length of the string by a given number and store it in another variable say 'k'.
k=len_str//num
# Check if the length of the string modulus given number is not equal to '0' or
# not using the if conditional statement.
if(len_str % num != 0):
    # If the statement is true, print "The given string cannot be divided into n equal halves".
    print("The given string cannot be divided into", num, "equal halves")
else:
  # Else loop from 0 to length of the string with the step size of the number 'k'
  # using the for loop.
    print("The given string after dividing into", num, "equal halves:")
    for i in range(0, len_str, k):
        # Slice from the iterator value to the iterator +n value using slicing and
        # print them.
        print(gvn_str[i:i+k])