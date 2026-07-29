import numpy as np

a = np.array([10, 20, 30])
b = np.zeros(5)
c = np.ones(3)
d = np.arange(1, 6)

print(a > 1) # gives true false output

# basic useful operations
a.sum()
a.mean()
a.max()
a.min()

#  2 dimensional array
matrix = np.array([[1, 2], [3, 4]])

# 3 dimensional array
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print (matrix)
print(tensor)