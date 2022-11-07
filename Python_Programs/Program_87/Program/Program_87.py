# Import the time module using the import statement.
import time

# creating a function time which counts the time


def countdownTime(tim):
    # A while loop is used in this function until the time reaches zero.
    while (tim):
       # To calculate the number of minutes and seconds, use divmod(). 
        timemins, timesecs = divmod(tim, 60)
    # Now, using the variable timeformat, output the minutes and seconds on the screen.
        timercount = '{:02d}:{:02d}'.format(timemins, timesecs)
    # By using end = '\n', we force the cursor to return to the
    # beginning of the screen (carriage return),
    # causing the following line written to overwrite the preceding one.
        print(timercount, end="\n")
    # The time. sleep() function is used to make the program wait one second.
        time.sleep(1)
    # Now decrement time so that the while loop can reach a finish.
        tim -= 1
    # After the loop is completed, we will print "The Given time is completed" to indicate the conclusion of the countdown.
    print('The Given time is completed')


# Then in seconds, Give the length of the countdown as user input and store it in a variable.
tim = input('Enter some random time = ')
# Convert the given time in seconds to integer data type using int() function.
tim = int(tim)

# Passing the given time as argument to the countdownTime() function
countdownTime(tim)