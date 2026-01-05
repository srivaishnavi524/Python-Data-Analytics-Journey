#creating a numpy ndarray object
#the array object in numpy is called ndarray
#array()
# import numpy as np
# x = np.array([1,2,3,4,5,6])
# print(x)
# print(type(x)) #<class 'numpy.ndarray'>
#-------------------------------------------------
# we can also pass a list, tuple or any array like object with array(). and it will be converted to ndarray
import numpy as np
# y = np.array((1,2,3,4,5,6))
# print(y)
# print(type(y)) #<class 'numpy.ndarray'>
#----------------------------------------------- 
#dimentions in Arrays
# a dimensions in array - a dimensions in array is one level of array depth(nested array)

# 0-D Arrays -  scalars, are the elements in an array, each value in an array is 0-D array.

#now we will create 0-d array with value 42

# import numpy as np
# x = np.array(42)
# print(type(x))
# --------------------------------
# 1-D array -  an array that has 0-D arrays as its elements is called uni directional or 1-D(collection of 0-D is called zero-dimensional array)

# import numpy as np
# a = np.array((1, 2,3,4,5, 6))
# print(a)
# -----------------------------------
#2-D array (2 arrays with certain values)(collection of 2D arrays is called one-dimensional array)

# import numpy as np
# x = np.array([[1,2,3,4],[5,6,7,8]])
# print(x)
# ---------------------------------------
# 3-D array with two 2-D array.(collection of two-dimensional array)
# import numpy as np

# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10, 11, 12]]])
# print(arr)
# a = arr[1][0][0] #to acess these elements we are using 3 supscripts so it is 3D 
# print(a)

# ------------------------------------
#check for dimensions of array : ndim attribute
import numpy as np
a = np.array(42)
b = np.array([1,2, 3, 4, 5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a.ndim) 
print(b.ndim)
print(c.ndim)
print(d.ndim)
#---------------------------------------
#creating 5-D array 
f = np.array([1,2,3,4,5], ndmin= 5)
print(f)
print("number of Dimensions: ", f.ndim)
f1 = f[0][0][0][0][3]
print(f1) # 4
#----------------------------------------
#Advantages of ND array :
