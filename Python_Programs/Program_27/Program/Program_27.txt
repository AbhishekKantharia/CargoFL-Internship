from collections import deque
# given string
givenstr = "HellothisisBTechGeeks"
# Printing the given string before reversing
print("Printing the given string before reversing : ")
print(givenstr)
# creating the stack from the given string
st = deque(givenstr)

# pop all characters from the stack and join them back into a string
givenstr = ''.join(st.pop() for _ in range(len(givenstr)))

# Printing the given string after reversing
print("Printing the given string after reversing : ")
print(givenstr)