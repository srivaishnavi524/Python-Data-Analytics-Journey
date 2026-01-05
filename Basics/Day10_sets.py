# Set in python 
# set is the collection of the unordered items.
# Each element in the set must be unique & immutable.
# nums={1, 2, 3, 4}
# set1={1, 2, 2, 3, 4, 2}
# print((type(set1))) #<class 'set'>
# print(set1) #repeated elements stored only once sp it resolved to {1, 2, 3, 4}
# null_set=set() #empty set syntax 
# print(null_set) # set()
#   #we cannot store list and dict in a set because they are immutable.bool,int, float, str, tuple this all can be stored in set
# collections={1, 2, 2, "hello", "world", "hello"}
# print(collections) # {1, 2, 'hello', 'world'} or {'world', 1, 2, 'hello'} it gives randomly 
# print(len(collections)) #4
#------------------------------------
# Set Methods 
# set.add(el) #adds an element
# set.remove(el) # remove 
#sets---> mutable 
#sets---> elements---> immutable(it checks for hashable values)
# set.clear()# empties the set
# collections.pop() #remove a random value
# print(collections)
#-----------------------------------
# set1={1,2,3,4}
# set2={4,5,6}
# print(set1.union(set2)) #combines both set values & return new set with unique values {1, 2, 3, 4, 5, 6}
# print(set1.intersection(set2))# combines common values & return new {4}
#-----------------------------------------------
# example 1
# you are giving a list of subjects for students. assume one classrom in required for 1 subject. how many classroom are needed by all students. 
# subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(subjects))
#--------------------------------------------
# example 2
# Figure out a way to store 9 &9.0 as seperate values in set.(you can take help of built-in data types)
# values ={9.0, "9"} 
# print(values)
#--------------------------------------------
