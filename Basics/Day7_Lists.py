#List:
# A built-in data type that stores set of values 
# it can store elements of different datatype (int, folat,string...)
# we can modify the list elements (mutable) , but strings are immutable. but we cannot add new elements in the list
# index starts from 0
# list allow duplicates
#-----------------------------
# marks=[94.5, 95.5, 97.7, 98.5, 99]
# print(marks) #display the list
# print(type(marks)) # clss type list
# print(marks[4]) # it prints 99
# print(len(marks)) #displays the total elements
# marks[4]=92 # we can modify the list elements
# print(marks)
"""Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")"""
#-----------------------------------------
#list Slicing
# list_name[staring_idx : end_index] #ending not included 
# marks=[87, 43, 25,  22, 44,55]
# marks[1:4] # [43, 25, 22]
# marks[:4 ] # 87 to 22 i.e, same as [0:4]
# marks[1: ] #same as [1: len(marks)]
# marks[-3:-1] # [22,44]

#----------------------------------
# list methods
# list =[2, 1, 3]
# print(list.append(4)) #return none but adds at the end when we print the list the element is added 
#  ####for every method it shows none but that action is done , we can only see changes when we print the list
# list.sort() # sort in ascending order 
# list.sort(reverse=True) # desc order
# list.reverse() #reverse order 3,1, 2
# list.insert(idx,el) # insert el at index
# list.insert(2,5)
# print(list) # 2,1,5,3
# list=[2,1,5,3]
# list.remove(1) #removes the first occurence of element [2,5,3]
# list.pop(idx) #removes element at idx
# list.pop() # removes only last item from list
# del list #The del keyword can also delete the list completely.
# he clear() method empties the list.The list still remains, but it has no content.
"""
change 2nd item in list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) 
------------------------------------
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
"""
#-------------------------------------
# list constructor
# list()
# Using the list() constructor to make a List:
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

#-----------------------------------------
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
list1=[1,2,3]
list2=[4,5,6]  
tuple1=(7,8)
list1.extend(list2) 
print(list1) #[1, 2, 3, 4, 5, 6] 
list1.extend(tuple1) #[1, 2, 3, 4, 5, 6, 7, 8]
print(list1) 
