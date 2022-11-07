# given two numbers
# given number a
number1 = int(input("Enter the first number:- "))
# given number b
number2 = int(input("Enter the second number:- "))
# finding bigger number of the given two numbers using if statement
if(number1 > number2):
    maxValue = number1
else:
    maxValue = number2
while(True):
    if(maxValue % number1 == 0 and maxValue % number2 == 0):
        print("The LCM of the given two numbers",
              number1, ",", number2, "=", maxValue)
        break
    maxValue = maxValue + 1