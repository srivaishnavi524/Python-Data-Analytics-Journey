# Splitting Numpy arrays
# Splitting is reverse operation of joining
# we use array_split() for splitting array, we pass it the array we a=want to split and number of splits.
import numpy as np
#split arrray into 3 parts
# arr = np.array([1,2,3,4,5,6,7,8])
# newarr = np.array_split(arr, 3)
# print(newarr)
"""[array([1, 2, 3]), array([4, 5, 6]), array([7, 8])]  """
#note : if there are less elements in the array than required, it will adjust from the end.

# we also have split() available but it will not adjust the elements when elements are less in source array for splitting
# accessing the splited array just like an array element
# print(newarr[0]) #[1 2 3]
# print(newarr[1]) #[4 5 6]
# print(newarr[2]) #[7 8]
#------------------------------------------
# splitting 2D array

# ar2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newar2 = np.array_split(ar2, 3)
# print(newar2)

# #output    [array([[1, 2],  [3, 4]]), array([[5, 6],[7, 8]]), array([[ 9, 10],[11, 12]])]

#---------------------
#splitting 2-D array into three 2-D along colums
ar3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newar3 = np.array_split(ar3, 3, axis=1)
print(newar3)
"""[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]"""
#--------------------------------------------
# An alternate solution is using hsplit() opposite of hstack() (no need or axis =1)
#Similar alternates to vstack() and dstack() are available as vsplit() and dsplit(). 