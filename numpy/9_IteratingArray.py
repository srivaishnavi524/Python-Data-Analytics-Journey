# ITERATING ARRAYS : 
# Iterating means going through elements one by one.

# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
import numpy as np
#iterate on elements of 1-D array
# arr1 = np.array([1,2,3])
# for x in arr1:
#     print(x)
"""output
1
2
3
"""
# Iterating elements of 2-D array
# arr2 = np.array([[1,2,3],[4,5,6]])
# for x in arr2:
#     print(x)
"""output
[1 2 3]
[4 5 6]
"""
# for x in arr2:
#     for y in x:
#         print(y)

"""output
1
2
3
4
5
6
"""
#iterating elements of 3-D array

# arr3 = np.array([
#     [[1,2,3],[4,5,6]],
#           [[7,8,9],[10,11,12]],
#           ])
# for x in arr3:
#     print(x)
"""output
[[1 2 3]
 [4 5 6]]
[[ 7  8  9]
 [10 11 12]]
"""

# for x in arr3:
#     for y in x:
#         for z in y:
#             print(z)

"""output
1
2
3
4
5
6
7
8
9
10
11
12"""
# Disadvantage of iterating through for loop:

#In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.

# ---------------------------------------------
#iterating arrays using nditer()
#The function nditer() is a helping function that can be used from very basic to very advanced iterations.

# Iterate through the following 3-D array:

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#   print(x)
# ----------------------------------------------
#Iterating Array With Different Data Types

#we use op_dtypes to change the datatype of array list to the expected datatype.
#NumPy does not change the datatype of elements directly. so it need some other space to perform this action. that extra space is called buffer, and in order to enable it in nditer() we pass     flags = ['buffered']

# arr = np.array([1,2,3])
# for x in np.nditer(arr, flags = ['buffered'], op_dtypes= ['S']):
#     print(x)
#-----------------------------------------------
# Iterating with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

#   1. arr[:, ::2]: This slices the array.
#     - : means "all rows".
#     - ::2 means "every 2nd element in columns".
#     - Result: [[1, 3], [5, 7]]

# 2. np.nditer(...): Iterates over the array element-wise.

#------------------------------------------------
# Enumerated Iteration Using ndenumerate()
#enumeration means mentioning seqence number of simthing one by one
#when we want the corresponding index while iteratig we use ndenumerate() method can be used.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
  """
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8 """