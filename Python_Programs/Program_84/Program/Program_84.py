# Import hashlib module using the import keyword
import hashlib

# Creating a reference/Instance variable(Object) for the hashlib module and 
# call sha3_384() function and store it in a variable
obj = hashlib.sha3_384()

# Give the string as user input using the input() function and store it in another variable.
gvn_str = input("Enter some random string = ")
# Convert the given string into byte string using the bytes() function by passing given string, 
# 'utf-8' as arguments to it 
gvn_str=bytes(gvn_str, 'utf-8')

# Call the update() function using the above created object by passing the above given string as 
# an argument to it
# Here it converts the given string in byte format to an encrypted form.
obj.update(gvn_str)
# Get the secure hash using the digest() function.
print(obj.digest())