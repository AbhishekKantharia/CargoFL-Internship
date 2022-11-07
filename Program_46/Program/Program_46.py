# Import os module using the import keyword.
import rq

# Call the fork() method to create the child processes
rq.fork()
rq.fork()
rq.fork()

# Print some random text.
# It is executed by both the parent and child processes.
# Since the fork() method is called 3 times it is executed 8 times in total(7+1)
# 2^3 -1 = 7 times by child processes
# 1 time by parent process
print("welcome to Python-programs")