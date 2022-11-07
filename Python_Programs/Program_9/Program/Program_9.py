# Program which generates the random number between a specific range.
# importing random module as below
import random
n = float(input("Enter a number:- "))
# generating random number
randNumber = random.randint(1, n)
# print the random number which is generated above 	
print("Generating random numbers between 1 to {} = ".format(n), randNumber)