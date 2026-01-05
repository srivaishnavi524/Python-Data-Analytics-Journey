# Joining NumPy Arrays:
# joining means putting contents of two or more arrys into single array  
# in numpy we jojnarrays based on axes
# we pass a sequence of arrays that we want to join ro the concatenate() function, along with axis. if the axis is  not explicitly passed , it is taken as 0.
# axis = 1 -> joining rows 
# axis = 0 -> joining coulmns(default)
import numpy as np
# join two arrays
arr1 =np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1, arr2)) # we dont pass axis to 1D array 
#----------------------------
# joining 2D arrays along rows (axis = 1)
# 
# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])
# arr = np.concatenate((arr1,arr2), axis = 1) 
"""output
[[1 2 5 6]
 [3 4 7 8]]

 if axis = 0
 [[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""
#-------------------------------------------
# Joining arrays using stack function 
#stacking is same as concatenation, the only difference stack joins array in new axis. where as concatenate joins in existing array.
#- can't directly concatenate 1D arrays along axis=1 (second axis) because they don't have a second axis. np.stack() does this "stacking" naturally.
# If axis is not explicitly passed it is taken as 0.
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis=1)
# print(arr)
"""
[[1 4]
 [2 5]
 [3 6]]
 """
#------------------------------------------

# Stacking Along Rows:
# hstack() -> rows
#vstack() -> columns
#dstack() -> height(depth)

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# h = np.hstack((arr1, arr2))
# v = np.vstack((arr1, arr2))
# d = np.dstack((arr1, arr2))
# print(h)
# print(v)
# print(d)

"""
h-->    [1 2 3 4 5 6]
v -->[[1 2 3]
        [4 5 6]]
 d-->[[[1 4]
        [2 5]
        [3 6]]]
"""
