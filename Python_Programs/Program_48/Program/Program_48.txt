# To utilize the method gethostbyname() in the socket library,
# first import the socket module using the import statement.
import socket
# To obtain the IP address of the host,
# we must give hostname as an argument to gethostbyname ().
# So, let's acquire our computer's hostname using the gethostname() method
# and send it as an argument to gethostbyname() to get the IP address.
# Also, assign the variable the value provided by the gethostbyname() method.

compIpAdress = socket.gethostbyname(socket.gethostname())
# Print the IP address of the computer.
print("The IP Address of this computer is [", compIpAdress, ']')