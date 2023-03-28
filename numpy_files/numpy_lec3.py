import numpy as np

x = np.array([1,2,3])
y = np.array((4,5,6))
t = np.array([[7,8,9],[10,11,12]])

z = np.concatenate([x,y])

# np.vstack() puts things vertically (on columns)
# np.hstack() puts things horizontally (on rows)
# np.dstack() creates a tensor (puts things on the depth)

w,m,n = np.split(z, 3) # same as np.split(z, [2,4]), pass how to split it in form of parts or list of indices

# np.vsplit() split on row
# np.hsplit() split on column
# np.dsplit() split on depth

print(w,m,n)

# we don't need to loop over the array in numpy. if we invoke something like result = 1/values, 
# it will automatically return an array where each value of result id 1/each value in values (keyword: vectorize)

