# Array are similar to list
# they dont have fixed side (flexble to work)
# they only have same type of elements
#homogeneous arrays will contain the elements of same data type.
#heterogeneous array may not be the same data type.

# we cannot directly use array . we should import array module i.e,   
# import array as arr
# import array (then use array only as array name)
#from array import * (if we need all modules use * otherwise specify perticular module name)
# array creation -  array()
# from array import *
# val = array( 'i' , [5, 9, -8, 4]) 
# print(val.buffer_info())
# TYPE CODES AVAILABLE FOR THE ARRAY MODULE FOR VARIOUS DATA TYPES 
# 1. 'i'- integer type-2 (signed integer) 
# 2. 'I' -integer type -2 (unsigned integer)
# 2. 'f' - Float type - 4 (float)
# 3. 'd' - Float type -8(double)
# 4. 'u' - unicode character - 2
# 5. 'l' - integer type - 4(signedlong)
# 6. 'L' - integer type - 4(Unsigned long)
# 7. 'q' & 'Q' -integer type  - 8 (signed/unsigned long long)
#-------------------------------------
# python array module
import array as myarray

#Creating an array
# arr = myarray.array('i',[1, 2, 3])
# arr1= myarray.array('d', [1.0, 2.1, 2.4, 2.5, 2.6])
# arr2= myarray.array("u", ['a', 'b', 'c', 'd'])
# #typecodes
# print(arr.typecode) #i
# print(arr1.typecode) # d
# print(arr2.typecode) #u
# #first look at the array
# print(arr)
# print(arr1)
# print(arr2)
# #printing the length of an array
# print(len(arr)) #3
# print(len(arr1)) #4
# print(len(arr2)) #5

# for i in range(0, len(arr)):
#     print(arr[i], end = " ")
# print("\n")
# for i in range(0, len(arr1)):
#     print(arr1[i], end = " ")
# print("\n")
# for i in range(0, len(arr2)):
#     print(arr2[i], end = " ")
#--------------------------------------
# INDEXING: for any array of the lenght n, the indexing will be the position at which each element is places in array.
#---------------------------------------
#assessing elements from an array using index values
# x =list(range(0,50,2))
# new_array = myarray.array('i', x)

# #printing the array
# for i in range(0, len(new_array)):
#     print(new_array[i], end=" ")
# print("\n")

# #accessing the element at index "20"
# print(new_array[20]) #41
#------------------------------------------
#creating an array
# new_arr = myarray.array('i', [3, 4, 5, 6, 7, 8, 9, 10])
#printing the new array
# for i in range(0, len(new_arr)):
    # print(new_arr[i], end=" ") #3 4 5 6 7 8 9 10 
# print(end="\n")
#adding elements in an array(we can add element in a perticular index)
# new_arr.insert(0,2) #element 2 is added into index 0

# new_arr.insert(0,1) # element 1 is added to index 0 , then the pervious elements move to next index
#printing the new array
# for i in range(0, len(new_arr)):
    # print(new_arr[i], end=" ") # 1 2 3 4 5 6 7 8 9 10
# print(end="\n")
#using append method(we can add element at the end of the array)
# new_arr.append(11)
# for i in range(0, len(new_arr)): 
    # print(new_arr[i], end=" ") # 1 2 3 4 5 6 7 8 9 10 11
# print(end="\n")
#----------------------------------------
#updating elements in array
# new_array=myarray.array('i', [1, 2, 2, 3, 4, 5])
# # printing array
# for i in range(0,len(new_array)):
#     print(new_array[i], end =" ")
# print(end="\n")
# # updating the array
# new_array[2] = 30 # assigning value 30 at index 2
# # printing array
# for i in range(0,len(new_array)):
#     print(new_array[i], end =" ")
# print(end="\n")
#--------------------------------------
# deleting elements in array 
# new_array.pop(2) # 2 is index value so element at index 2 is 30 is deleted from array
# for i in range(0,len(new_array)):
#     print(new_array[i], end =" ")
# print(end=" ")
#------------------------------------------
# SLICING: is the process of getting a sequence from the data structure which we have a starting index and ending index  (ending index is not included)
#slicing operations in an array
# x = list(range(0,50,2))# start 0 default also 0 , stop 100, step 3 default is 1
# slice_array = myarray.array('i', x)
# for i in range (0, len(slice_array)):
#     print(slice_array[i], end=" ") # printing elements in array list 0 to 50 
# print(end="\n")

#slicing operations
# slice_arr1= slice_array[10:20]
# for i in range(0,len(slice_arr1)):
#     print(slice_arr1[i], end=" ") # printing elements from index 10 to 19
# print(end="\n")

#negative indexing
# slice_arr2 = slice_array[10: -10] 
# for i in range(0, len(slice_arr2)): # print elements from starting 10th element to 10th element from last (20 to 28)
#     print(slice_arr2[i], end=" ")
# print(end="\n")
# reversing the order [: : -1]
#------------------------------------
#searching operations using index()
# x  = list(range(0, 100,5))
# search_array = myarray.array('i',x)
# for i in range(0, len(search_array)):
#     print(search_array[i], end=" ")
# print(end ="\n") 
# #print first 10 elements of the array
# for i in range(0,len(search_array[0:10])):
#     print(search_array[i], end = " ")
# print(end="\n")
# #search the number 15 in the array index
# index = search_array.index(15) #to find index of element 15
# el =  search_array[index] # it gives the element which is present in index
# print(index,el) # 3  15
#-------------------------------------------
#sorting operations
# sort_array=myarray.array('i', [5,3,4,6,9,7,8])
# sorted_array=sort_array.tolist() #covert array to list
# # ascending order
# sorted_array.sort()
# print(sorted_array)
# #descending order
# sorted_array.sort(reverse=True)
# print(sorted_array)
#-----------------------------------------
# Array values from user in python
# from array import *
# arr=array('i', [])
# n = int(input("Enter the lenght of array :"))
# for i in range(n):
#     x= int(input("enter the next value: "))
#     arr.append(x)
# print(arr) 
# #searching a element in array
# val =int(input("enter a value for search "))
# idx = 0
# for e in arr:
#     if e==val:
#         print("the element present in index ", idx)
#         break
#     idx+=1
#--------------------------------------------
