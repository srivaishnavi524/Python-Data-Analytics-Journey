# Function : Block of statements that perform a specfic task.

# def func_name(param1, param2...): --> function defination 
#     #some work
#     return val
#--------------------------------------
#pass by value (passing the value of a)
# & pass by reference(passing the address of 10 )
#in python we dont have this pass by value and pass by reference 
# because here x and a refers to same object even through we call them by value. so perticularly we dont have pass by value or reference
# def update(x):
#     x=8
#     print("x : ",x )
# a = 10
# update(a)
# print("a :", a)
# print(id(a)) # gives the object address
#--------------------------------
# func_name(arg1, arg2...) # function call
# def sum(a, b):
#     sum =  a + b
#     print(sum)
#     # return sum
# sum(3, 4)
# sum(2, 3)
#-------------------------------
# sep=" " #is by default give the space between the words if we seperate them by coma 
# print("hello", "world") # hello world
# end =" " # if we want to print the next statement in same line then we us end = " "
# print("hello", end=" ")  #end =" " gives space, end =" \n" print in next line , end ="$" print $ in middle of that statements
# print("world")
# functions types 
# 1. Built-in functions 
# print()
# len()
# type()
# range()
# 2. User Defined functions 
#-------------------------
# default parameters: assigning a default value to parameter, which is used when no argument is passed 
# ex:
# def cal_sum(a=2, b=3): # we can pass 1 default and we can give another parameter in calling also
#     print(a + b)
#     return a+ b
# cal_sum() # if we dont provide any parametrs it takes 2 and 3 as defaultparameters because we initilized in the func defination
# cal_sum(4, 5)
#-------------------------------
# def cal_sum(a, b=3): # we can pass 1 default and we can give another parameter in calling also
    # print(a + b)
    # return a+ b
# cal_sum(4) # we cannot give default only to a and leave b directly it shows error i.e, we should give default to last parameter 
#----------------------------------
# WAF to print the length of a list.(list is the parameter )
# cities = ["hyderabad","chennai","banglore","delhi","mumbai"]
# nums = ["1", "2", "3", "4"]
# def print_len(list): #we can mention as cities or nums
    # print(len(list)) #we can mention as cities or nums
# print_len(nums)
# print_len(cities)
#------------------------------
# WAF to print the elements of a list in a single line. (list is the parameter)
# nums = ["1", "2", "3", "4", "5"]
# def print_list(nums):
#     print(nums)
# print_list(nums) #['1', '2', '3', '4', '5'] (below methid is correct)
# or 
# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(nums) # 1 2 3 4 5  (direct items will display here )
#---------------------------------
# WAF to find factorial of n (n is parameter)
# n =int(input("enter a number to find factorial : "))
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print("factorial of a number is :", fact)
# cal_fact(n) #  if n is 5 then factorial is 120
# cal_fact(3) # 5

#-----------------------------
# WAF to convert USD to INR
# def converter(usd_val):
#     inr_val= usd_val*83
#     print(usd_val, "USD = ", inr_val, "INR")
# converter(2) #2 USD =  166 INR
#----------------------------------
# WAF to find the given number is even or odd
# num = int(input("enter a number :"))
# def even_odd(num):
#     if num%2!=0:
#         print("ODD")
#     else:
#         print("EVEN")
# even_odd(num)
# even_odd(5) # it directly display As ODD
#-----------------------------------
# def sum(a, *b): # a is 6 and remaining values are for b so it is tuple b 
#     c = a 
#     for i in b:
#         c = c+i
#     print(c)
# sum(5,6,7,9)
#--------------------------------
# Keyword , variables , arguments (kwargs)
# to print data of a person
# def person(name, **data): # **takes multiple arguments 
#     print(name)
#     for i,j in data.items():
#         print(i, j)
# person('Sri vaishnavi', age=20,city="hyderabad", mob=123456)
#----------------------------------
#fibonacci series
# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)
#--------------------------------
# print fibonacci numbers less than 100i.e, between 0 to 100
# def fib99(n):
#     a =0
#     b=1
#     if  n<=0:
#         print("invalid input")
#     elif n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,100):
#             c = a+b
#             a = b
#             b = c
#             if b > 100:
#                 break
#             print(c)
# fib99(100)
#-----------------------------
# def print_fibonacci(limit):
#     a, b = 0, 1
#     if limit <= 0:
#         print("Invalid input")
#     else:
#         print(a)
#         for i in range(limit):  # Just a big enough number
#             if b > limit:
#                 break
#             print(b)
#             a, b = b, a + b
# # print_fibonacci(100)
# print_fibonacci(150)
#--------------------------------
# Anonymous functions: functions without name /lambda function
#if we want to use a function only single time and that function doesnot have multiple lines code(single line/single expression) then we use this function
 
# def add(x,y):
#     return x+y
# res=add(10,5)
# print(res)
#method 1
# res = lambda x , y : x + y 
# print(res(3,6)) 
#method 2
# res1 = (lambda x,y : x+y)(6,3) #we can call only once because it does not have any function name 
# print(res1)
# example 1
# res2 = (lambda x,y : x if x > y else y)(7, 3)
# print(res2)
# example 2
# res3= (lambda num: "Even number" if num%2 ==0 else "Odd number")(5)
# print(res3)
