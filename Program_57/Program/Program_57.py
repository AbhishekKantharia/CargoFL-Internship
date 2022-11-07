# function which returns true if the given number
# is evennum or oddnum using recursoive approach


def checkPrimeRecursion(numb):
  # Defining the base condition as an integer less than two.
    if (numb < 2):
      # Then return the result and determine whether the number is even or odd.
        return (numb % 2 == 0)
    # Otherwise, use the number -2 to invoke the function recursively.
    return (checkPrimeRecursion(numb - 2))


# Give the number as static input.
numb = int(input('Enter some random number = '))
# passing the given number to checkPrimeRecursion
# if the returned value is true then it is even number
if(checkPrimeRecursion(numb)):
    print("The given number", numb, "is even")
# if the returned value is false then it is odd number
else:
    print("The given number", numb, "is odd")