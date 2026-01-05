# Filtering Arrays
# getting some elemets out of an existinf array and creating a new array form it is called filtering
# in numpy , we fileter an array using boolean index list 
#boolean index list is a list of bololeans corresponding to the indexes of array
# True-> filtered array
# False -> excluded from the filtered array

# Create an array from the elements on index 0 and 2:

import numpy as np

# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr) #[41, 43]
#------------------------------
# creating filter  array using if-else 
# arr = np.array([4, 5, 6, 7])
# filter_arr = []
# for el in arr:
#     if el >5:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# new_arr = arr[filter_arr]

# print(filter_arr) # [boolean list]
# print(new_arr) # new array list

#----------------------------------------------
# creating filter directly from array 
arr1 = np.array([1,2,3,4,5,6,7,8,9])
filter_arr1 = arr1 > 2 # gives T or F
new_aar1 = arr1[filter_arr1]
print(filter_arr1) #[False False  True  True  True  True  True  True  True]
print(new_aar1) #[3 4 5 6 7 8 9]
