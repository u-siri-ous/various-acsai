import numpy as np

np.random.seed(0)   # makes the random numbers predictable
                    # With the seed reset (every time), the same set of numbers will appear every time.
                    # np.random.seed() is NOT threadsafe

var = np.random.randint(10, size=6)     # 1 dimensional array
mat = np.random.randint(10, size=(3,4)) # 2 dimensional array

print(mat.ndim)         # dimension
print(mat.size)         # how many elements
print(mat.dtype)        # datatype of each entry
print(mat.itemsize)     # size of each entry
print(mat.nbytes)       # size in bytes of matrix

# accessing elements -> arrays are indexed like lists 
# for matrices and n-dimensional arrays -> we put everything in a single set of square brackets
# slicing works the same as lists

print(mat)
print(mat[0,0]) # first entry on first row

a = np.arange(1,10)   #creates [0,1,2,3,4,5,6,7,8,9]
t = np.reshape(3,-1)      #creates a 3X(X) matrix from array, -1 leaves column number to interpreter
print(t)

# slicing in multidimensional array
x = mat[:2, :3]     # takes the first two rows and the first tree columns, output is a 2X3 matrix
y = mat[:2, ::2]    # takes the first two rows and columns with a step of two, output is a 2X2 matrix
z = mat[::-1, ::-1] # reverses on x and y axis

# access a row or a column
b = mat[:,2]    # takes the third column of mat, for rows it's common indexing
                # prints in form of row

