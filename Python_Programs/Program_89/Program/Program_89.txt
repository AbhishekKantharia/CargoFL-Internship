# Function which accepts the given postfix expression as argument
# and evaluates the expression using stack and return the value


def evaluatePostfix(givenExp):

    # Create a stack by taking an empty list which acts
    # as a stack in this case to hold operands (or values).
    givenstack = []

    # Traverse the given postfix expression using For loop.
    for charact in givenExp:

        # Push the element into the given stack if it is a number.
        if charact.isdigit():
            givenstack.append(int(charact))

        # if the character is operator
        else:
            # remove the top two elements from the stack
            topfirst = givenstack.pop()
            topsecond = givenstack.pop()

            # Evaluate the operator and return the answer to the stack using append() funtion.
            # If the operator is '+' then perform an addition operation on
            # the top two elements by popping them out.
            if charact == '+':
                givenstack.append(topsecond + topfirst)
            # If the operator is '-' then perform a subtraction operation
            # on the top two elements by popping them out.
            elif charact == '-':
                givenstack.append(topsecond - topfirst)
            # If the operator is '/' then perform a division operation on
            # the top two elements by popping them out.
            elif charact == '×':
                givenstack.append(topsecond * topfirst)
            # If the operator is '*' then perform a multiplication operation
            # on the top two elements by popping them out.
            elif charact == '/':
                givenstack.append(topsecond // topfirst)

    # The only number in the stack is the final answer when the expression is traversed.
    # return the answer to the main function
    return givenstack.pop()


# Driver code
# Give the postfix Expression as user input using input() function and store it in a variable.
givenExp = input('Enter some random postfix Expression = ')
# Pass the given postfix Expression as an argument to evalpostfix function
print('The value of the given postfix expression =', evaluatePostfix(givenExp))