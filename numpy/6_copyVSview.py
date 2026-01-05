# difference between numpy array copy and view.

# the main difference between copy and view is that the copy is a new array, the view is just a view of the original array

# copy owns the data and any changes made to the copy will not affect original array. and changes made to the original array will not affect the copy.

#view does not own the data and any changes made to the view will affect the original array , and changes made to the original array affect the view.
import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42

# print(arr) #[42  2  3  4  5]
# print(x) #[1 2 3 4 5]

#make changes to array
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)
# OP 
# [42  2  3  4  5]
# [42  2  3  4  5]

#make changes to view 
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)
# OP 
# [31  2  3  4  5]
# [31  2  3  4  5]