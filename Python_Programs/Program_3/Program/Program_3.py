# given number
number = int(input("Enter the number of your choice :-"))
# intializing a temporary variable with False
temp = False
# We will check if the number is greater than 1 or not
# since prime numbers starts from 2
if number > 1:
    # checking the divisors of the number
    for i in range(2, number):
        if (number % i) == 0:
            # if any divisor is found then set temp to true since it is not prime number
            temp = True
            # Break the loop if it is not prime
            break
if(temp):
    print("The given number", number, "is not prime number")
else:
    print("The given number", number, "is prime number")