#Array indexing is the same as accessing an array element. start with 0, second 1
# import numpy as np
# a = np.array([1,2,3,4,5])
# print(a[0]) # 1
# b = np.array([[1,2,3],[4,5,6]])
# print(b[1, 0]) # 4
# c = np.array([[[1,2,3],[4,5,6]],   
#               [[7,8,9],[10, 11, 12]]])
# print(c[1, 1, 0]) # 10    
# --------------------------------------
#negative indexing: use negative indexing to access an array from the end
# import numpy as np
# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# print(arr[-1,-1,-2 ]) # 11
# print(arr[-2, -2, -3]) # 1 (total negative values)
# print(arr[1, 1, -1]) # 12 (combination of negative and positive)

# # adding the elements from arrays
# print(arr[0,0,2]+ arr[1,0,2]) # 3 + 9 = 12

#----------------------------------------
import numpy as np
d = np.array([
    [ [[1,2],[3,4],[5,6]] ],  
    [ [[10,20],[30,40],[50,60]] ],
    [ [[100,200],[300,400],[500,600]]],
    [ [[11,22],[33,44],[55,66]] ]
])
print(d[1, 0, 1, 1])  # 40 
print(d[3, 0,2,1])    # 66 
print(d[2, 0, 1, 0])  # 300


"""np.array([
    [ [ [1,2],[3,4],[5,6]] ],            main element [idx]    box 1[0] [0][0 or 1 or 2][ 0 or 1]
    [ [ [10,20],[30,40],[50,60]] ],                                     box 2[1] [0][0 or 1 or 2][0 or 1]
    [ [ [100,200],[300,400],[500,600]]],                         box3[2]  [0][0 or 1 or 2][0 or 1]
    [ [ [11,22],[33,44],[55,66]] ]                                       box4[3]  [0][0 or 1 or 2][0 or 1]
])
"""