# shape of an array - the shape of the array is the number od elements in each dimensions.
#we access the array shape using arr.shape
import numpy as np

a = np.array(42)
b = np.array([1,2, 3, 4, 5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a.shape)   # ( )
print(b.shape)  #  (5,)
print(c.shape)  #  (2, 3)  # first dimentions has 2 elements and second has 3 elements
print(d.shape)  # (  2, 2, 3 ) #overall 2 elements each elements has 2 sub elements , and that sub has 3 elements 

f = np.array([1,2,3,4,5], ndmin= 5)
print(f) #   [[[[[1 2 3 4 5]]]]]
print(f.shape) # (1, 1, 1, 1, 5)

# shape represents in tuple
# #in the above  the shape has 5 elements so it is 5 dimentional array
