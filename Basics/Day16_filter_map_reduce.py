#lambda functions in day 13
# filter()
# map()
# reduce()
# data -> chunk that data-> filter it-> map it-> reduce it
# filter(): based on the data we should apply the condition and take the output
# it accepts 2 parameters(function, iterable list or tuple or set)
#map(): it accepts 2 functions , for each value we should get the output
#reduce(): from the data we should get single output
# def is_even(n):
#     return n%2==0
# ----------------------------------------
#example 1
from functools import reduce

# nums = [3, 2, 6, 8, 4, 6, 2, 9]
# evens = list(filter(lambda n : n%2 ==0,nums)) # we cant directly use filter because its takes values as objects and give o/p in objects . so we should convert them into list or tuple
# print(evens) 
# doubles = list(map(lambda n : n *2 , evens))
# print(doubles)
# sum = reduce(lambda a,b : a+b ,doubles)
# print(sum)
#------------------------------------------
# example2  (filter)
# list1 = [1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x : x%2 ==0, list1)))
# print(list(filter(lambda x : x%2 != 0, list1)))
#-------------------------------------------
# example 3 (remove empty string from the list)
# names =["ram", "naveen", "raj", "","", "harry", ""]
# print(list(filter(None,names))) #None is used to remove the none values in the list
#-------------------------------------------
# example 4 (consider the age of people who is above 18 for voting) 
# list2=[34, 52, 13, 15, 78, 22, 19, 18]
# print(list(filter(lambda x :  x>18 , list2)))
#-------------------------------------------
# example 5 print only the numbers which are divisible by 3
# tup= (3, 4, 15, 12, 16, 18)
# print(tuple(filter( lambda num : num%3 == 0, tup)))
#-----------------------------------------
#print the items which are less than 90
# item = [("soap", 55),("rice", 50),("oil", 110),("tomato", 20)]
# print(list(filter(lambda item : item[1]<= 90, item )))
#---------------------------------------------
# map() 
# example 1 print the sqrt of the given elements
# tup1 =(1,2,3,4,5,6,7,8,9,10)
# print(tuple(map(lambda x : x**2, tup1)))
#---------------------------------------------
#example 2  adding two tuples
# tup2 =(1,2,3,4,5,6,7,8,9,10)
# tup3 =(1,2,3,4,5,6,7,8,9,10)
# print(tuple(map(lambda x,y : x+y, tup2,tup3)))
#---------------------------------------------
# reduce() : to use this function we should 
# import reduce from functools as, 
# from functools import reduce
set1 ={1,2,3,4,5,5,6,7,8,9,10}
print(reduce(lambda x,y : x+y, set1)) #55
print(reduce(lambda x,y: x*y, set1))