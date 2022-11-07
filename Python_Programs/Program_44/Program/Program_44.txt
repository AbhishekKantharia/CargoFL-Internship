# Give the first string as User input  using the input() function , convert the given string into lower case
# using built-in lower() method and store it in a variable.
fst_strng = input("Enter some Random String = ").lower()
# Give the  second string as User input  using the input() function, convert the given string into lower case
# using built-in lower() method and store it in another variable.
secnd_strng = input("Enter some Random String = ").lower()
# Get the Common characters between both the above given strings using built-in
# intersection() method which is a set method.
# Sort the above given string using  built-in sorted() method.
# Join the the above given string using built-in join()method .
# Print all the Common Characters between the above given two Strings.
print("The Common Characters between the above given two Strings = ",
      ''.join(sorted(set.intersection(set(fst_strng), set(secnd_strng)))))