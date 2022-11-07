# Give the String as user input using the input()function and store it in the variable.
gvn_str = input("Enter some random String = ")
# Take a variable say 'count' and initialize it's value with '0'
count_no = 0
# Loop from 0 to the length of the above given String using For Loop.
for itrtor in gvn_str:
    # Inside the loop, check whether  if the value of iterator is alphabet or
    # using built-in isalpha() method inside the if conditional statement.
    if(itrtor.isalpha()):
     # If the given condition is true ,then increment the above initialized count value by '1'.
        count_no = count_no+1
# Print the number of Alphabets in a given string by printing the above count value.
print(
    "The Number of Characters in a given string {", gvn_str, "} = ", count_no)