# 1. Linear Search(unsorted or sorted order)
# 2. Binary Search (sorted order)
#----------------------------------------------
#linear search
# using while loop 
# list = [4,6,9,5,8]
# n = 9
# pos = -1
# def search(list, n):
#     i = 0
#     while i<len(list):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#         i = i+1

# if search(list, n):
#     print("FOUND at", pos)
# else:
#     print("NOT FOUND")
# --------------
#using for loop

# list = [1,7,9,5,0,10]
# n=5
# for i in range(len(list)):
#     if list [i] == n:
#         print("element found at " , i+1)
#         break
# else:
#         print("not found")
#----------------------------------------------
# If the list length is increseas linear search is time taking process
#Binary Search

# pos = -1
# def search(list, n):
#     l = 0
#     u = len(list)-1 #index values
#     while l <=u:
#         mid = (l+u) // 2
#         if list[mid] ==n:
#             globals() ['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid + 1
#             else:
#                 u = mid - 1
#     return False

# list=[1,3,5,8,10, 14, 24, 33, 66, 78, 88, 93, 99, 102]
# n = 24
# if search(list, n):
#     print("Found at", pos+1)
# else:
#     print("Not Found")

    
