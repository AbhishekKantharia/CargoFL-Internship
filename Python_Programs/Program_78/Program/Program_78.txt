# Import numpy module using the import keyword
import numpy as np
            
# Create a matrix(3-Dimensional) using the matrix() function of numpy module by passing 
# some random 3D matrix as an argument to it and store it in a variable
gvn_matrx = np.matrix('[2, 4, 1; 8, 7, 3; 10, 9, 5]')
            
# Pass the index(row, column) and item/value as an argument to the itemset() function and 
# apply it to the given matrix.
# Here it inserts the given item at the specified index in a matrix(inserts 100 at 1st row, 2nd col).
# Store it in another variable
gvn_matrx.itemset((1, 2), 100)
# Print the given matrix after inserting an item at the specified index
print("The given matrix after inserting an item {100} at the specified index(1st row, 2nd col):")
print(gvn_matrx)