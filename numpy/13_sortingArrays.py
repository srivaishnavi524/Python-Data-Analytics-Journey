# Sorting Arrays
#sorting means putting elements in an ordered sequence 
#sequencing in numeric / alphabetical, ascending or descending
# the numpy ndarry object has a function called sort() that will sort a specified array
import numpy as np

# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr)) #[0 1 2 3]
# print(arr) #[3 2 0 1] ->sort method returns just copy of array, original array remains same.

strr= np.array(['banana', 'cherry', 'apple'])
print(np.sort(strr)) #['apple' 'banana' 'cherry']

#we can sort boolean array[True, False , True ]-> [False, True, True]

#sorting 2-D array 
# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))
"""[[2 3 4]
 [0 1 5]]"""