# function which computes and returns the highest common factor of the given two numbers
def findGcd(number1, number2):

    # finding the smaller number
    if number1 > number2:
        smallNumber = number2
    else:
        smallNumber = number1
    # using for loop to traverse from 1 to smaller number
    for i in range(1, smallNumber+1):
      # if it divides the given two numbers without leaving the
      # remainder then assign result it with that loop iterator value
        if((number1 % i == 0) and (number2 % i == 0)):
            result = i
    # return the final result which is greatest common divisor(GCD)
    return result


# given two numbers
# given number a
number1 = int(input("Enter the first number:- "))
# given number b
number2 = int(input("Enter the second number:- "))
# passing the given two numbers to findGcd function which returns the greatest common factor of the given two numbers
ans = findGcd(number1, number2)
# print the hcf of the given two numbers
print("The Highest Common Factor (HCF) of the numbers", number1, number2, "=", ans)