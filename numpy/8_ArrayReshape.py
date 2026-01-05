# Reshaping array : changing the dimension of the array
# the shape of an array is the number of elements in each dimension.
#by reshaping we can add or remove elements or change dimension of an array
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#(1D to 2D)
# newarr = arr.reshape(4, 3)  #array has 4 main elements/array and each element should have 3 elements  
# print(newarr)
""" output   
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]] """

# 1D to 3D
newarr1 = arr.reshape(2, 3, 2) # main 2  , sub 3 , each has 2 elements 
print(newarr1)
""" output
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]] """
# can we reshape into any shape?
# yes, as long as the elements required for reshaping are equal in both shapes

#We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

# arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr2 = arr.reshape(3, 3)
# print(newarr2) #ValueError: cannot reshape array of size 8 into shape (3,3)

# Returns copy or view ? 
# check if the returned array is a copy or a view:

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arr.reshape(2, 4).base) #original array
# print(arr.base) #none
# reshape means view
# - If the array is a view (created using reshape, slice, etc.), .base returns the original array.
# - If the array is not a view (it's the original array), .base returns None.

#Unknown dimension
#You are allowed to have one "unknown" dimension.

# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

# Pass -1 as the value, and NumPy will calculate this number for you.

# Convert 1D array with 8 elements to 3D array with 2x2 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

#note :  We can not pass -1 to more than one dimension.

#-------------------------------------
# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.

# We can use reshape(-1) to do this.

# Convert the array into a 1D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.