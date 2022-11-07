# Import numpy module using the import keyword
import numpy as np
            
# Create a matrix(2-Dimensional) using the matrix() function of numpy module by passing 
# some random 2D matrix as an argument to it and store it in a variable
gvn_matrx = np.matrix('[10, 1; 2, 7]')
# Print the given matrix
print("The given matrix is:") 
print(gvn_matrx)   

# Apply partition() function on the given matrix by passing some random index value as an argument to it
# to partition the given matrix.
gvn_matrx.partition(1)
# Print the given matrix after partition.
print("The given matrix after partition is:")
print(gvn_matrx)