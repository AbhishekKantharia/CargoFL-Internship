# given number
number = int(input("Enter the given number:- "))
# printing the factors of given number
print("printing the factors of given number : ")
# using for loop
for i in range(1, number+1):
    # checking if iterator divides the number if so then print it(because it is factor)
    if(number % i == 0):
        print(i)