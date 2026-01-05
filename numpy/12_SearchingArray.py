# Searching Arrays: we can search an array element ,and return the indexes that matched
#to search an array use where() method
#-------------------------------------------
import numpy as np
# find the index where the value is 4:
arr = np.array([1,2,3,4,5,6,7,4,4,4])
x = np.where(arr == 4)
# print(x) #  (array([3, 7, 8, 9]),) -> index 

eve = np.where(arr%2 == 0)
# print(eve) #(array([1, 3, 5, 7, 8, 9]),)
#--------------------------------------------
#search sorted:
# searchsorted() which performs a binary search in the array, and return the index where the specified value would be inserted to maintain sorted order.

#find the index where the value 4 should be inserted
s = np.array([3, 5, 6, 7, 8])
# new_s = np.searchsorted(s, 4)
# print(new_s) # 1 
#search from right side
r = np.array([3,4,5,7,9])
right = np.searchsorted(r ,4 , side = 'right')
print(right) 
#if the element is not in the list it gives same from left and right (exact position where it belongs to)
"""
- Index counting is always from left in NumPy/Python.
- left: insert before the element (4 → index 1)
- right: insert after the element (4 → index 2)

So for [3, 4, 5, 7, 9]:
- 4 is at index 1.
- Insert before 4 (left) → index 1.
- Insert after 4 (right) → index 2.
"""