# A permutations refers to an  arrengement of elements. e.g : [3, 2, 1] is a permutation of [1, 2, 3] and vise- versa.
#the NumPy random module provides two methods for this : shuffle() and permutation().
#shuffle( ) method will make changes too the original array
#permutation(): this method will not change the original array.
from numpy import random
import numpy as np
#now we will randomly suffle elements for the below array.

# arr = np.array([1,2,3,4,5])
# random.shuffle(arr)
# print(arr) #randomly array will shuffle the elements

#now we will generate a permutation of elements for the below array:
arr2 = np.array([1,2,3,4,5])
new_arr2 = random.permutation(arr2)
print(arr2) # original array
print(new_arr2) # changed array

