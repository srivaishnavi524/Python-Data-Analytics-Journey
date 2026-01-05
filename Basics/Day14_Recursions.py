# Recursion : When a function calls itself repeatedly 
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5) # 5  4   3  2  1   0(terminate)
#call stack : a portion of memory that keeps track of the active function calls during program execution. It operates on a Last-In, First-Out (LIFO) principle, much like a stack of pancakes or books. 
#------------------------------
# factorial of N 
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1) * n  #n!= (n-1)! * n recurrence relation
# print(fact(6))  #6= 720 , 3=6
#------------------------------
# WAP to cal sum of first n natural numbers
# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1) + n
# cal = sum(4)
# print(cal)
#-------------------------------------
# Write a recursive function to print all elements in a list (use list & index as parameters)
# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["mango", "banana", "apple", "guva", "orange"]
# print_list(fruits)
#--------------------------------
#factorial using recurrsion
def facto(n):
    if n==0:
        return 1
    return n * facto(n -1)
result=facto(5)
print(result)
#-------------------------------

