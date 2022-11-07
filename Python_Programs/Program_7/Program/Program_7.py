# implementing stack data structure in Python


# Creating new empty stack
def createStack():
    Stack = []
    return Stack
# Checking if the given stack is empty or not


def isEmptyStack(Stack):
    return len(Stack) == 0


# appending elements to the stack that is pushing the given element to the stack
def pushStack(stack, ele):
    # appending the given element to the stack using append() function
    stack.append(ele)
    # printing the newly inserted/appended element
    print("New element added : ", ele)


# Removing element from the stack using pop() function
def popStack(stack):
  # checking if the stack is empty or not
    if (isEmptyStack(stack)):
        return ("The given stack is empty and we cannot delete the element from the stack")
    # if the stack is not empty then remove / pop() element from the stack
    return stack.pop()

# function which returns the top elememt in the stack


def topStack(stack):
  # returning the top element in the stack
    return stack[-1]


# creating a new stack and performing all operations on the stack
# creating new stack
st = createStack()
# adding some  random elements to the stack
pushStack(st, int(input("Enter the number whose value is to be pushed into the Stack:- ")))
pushStack(st, int(input("Enter the number whose value is to be pushed into the Stack:- ")))
pushStack(st, int(input("Enter the number whose value is to be pushed into the Stack:- ")))
pushStack(st, int(input("Enter the number whose value is to be pushed into the Stack:- ")))
pushStack(st, int(input("Enter the number whose value is to be popped out of the Stack:- ")))
# removing element from stack
print(popStack(st), "is removed from the Stack")
# printing the stack after removing the element
print("Printing the stack after modification", st)
# printing the top element from the stack
print("The top element from the Stack is ", topStack(st))