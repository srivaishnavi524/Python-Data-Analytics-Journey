# Python : String Integer float boolean complex 
# Datatypes in Numpy:
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex
# m - timedelta
# M -  datetime
# O - object
# S - string
# U unicode String
# V - memory 

#checking datatype of array -  dtype
import numpy as np

# a = np.array([1,2,3,4])
# print(a.dtype) # int32
# b = np.array(['apple', 'banana','watermelon'])
# print(b.dtype) #<U10  -> U is unicode string , 10 is max no. of elements in a string

# c =  np.array([1,2,3,4], dtype ='S')
# print(c)  #[b'1' b'2' b'3' b'4']
# print(c.dtype)  #|S1

# d =  np.array([1,2,3,4,5], dtype ='i4')
# print(d)  # [1 2 3 4 5]
# print(d.dtype)  #int32

#if a type is given in which the elements cannot be casted then numpy will raise error. what if a value cannot be converted?
# c =  np.array(['a' , '1', '3'], dtype ='i')
# print(c)  
# print(c.dtype) # ValueError: invalid literal for int() with base 10: 'a' 

#converting data type in existing array - astype()
c =  np.array([1.1,2.1,3.1,4.1])
c1 = c.astype('i')
print(c1)  #[1 2 3 4]
print(c1.dtype)  #int32

# to change from integer to boolean [1, 0, 4, 5] o/p is [True False True True]
