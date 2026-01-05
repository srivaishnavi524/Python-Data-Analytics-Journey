# slicing arrays:it means taking elements from one given index to another given index 
#[start:end] , [start:end:step]
# default values start - 0, send - len of array , step - 1
import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6]) # index values [0 1 2 3 4 5]
# print(arr[4:])  # idx 4 to end [ 5 6]
# print(arr[:4]) # beginning to 4( 4 idx not included) [1 2 3 4 ]

#negative Slicing

# print(arr[-4: ]) # [3 4 5 6]
# print(arr[-6:-1]) # [ 1 2 3 4 5]

#step
# 1-D array
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(arr1[1:10:2]) # [ 2 4 6 8 10]
# print(arr1[1::2]) # [ 2 4 6 8 10]
# print(arr1[:5:1]) #[ 1 2 3 4 5 ]
# print(arr1[1::3]) #[2 5 8]
# #negative slicing
# print(arr1[10::-1]) #reverse order of array

# 2-D array
arr2 =np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr2[0:3,1:4])  # [[2 3 4] [7 8 9]]
print(arr2[0:3,3]) # from both elements return index 3  [4 9]
print(arr2[0:4, 4])  #[ 5 10]
print(arr2[1, 0:4]) #from 2nd element slice 0 : 4 [6 7 8 9]
print(arr2[0:2, 1:4]) #from both slice from 1 to 4     [[2 3 4] [7 8 9]]
