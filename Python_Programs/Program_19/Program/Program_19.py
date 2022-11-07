# given number
given_num = 12321
# taking another variable to store the copy of original number
# and initialize it with given num
duplicate_num = given_num
# Take a variable reverse_number and initialize it to null
reverse_number = 0
# using while loop to reverse the given number
while (given_num > 0):
    # implementing the algorithm
    # getting the last digit
    remainder = given_num % 10
    reverse_number = (reverse_number * 10) + remainder
    given_num = given_num // 10
# if duplicate_num and reverse_number are equal then it is palindrome
if(duplicate_num == reverse_number):
    print("The given number", duplicate_num, "is palindrome")
else:
    print("The given number", duplicate_num, "is not palindrome")