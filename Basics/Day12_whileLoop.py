#printing numbers from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i+=1
# print("end of loop") 
#---------------------------------------------
# i=100
# while i>=1:
#     print(i)
#     i-=1
# print("end of loop printing 100 to 1")    
#---------------------------------------------
# printing a multiplication table
# n=int(input("enter a number: "))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1
#----------------------------------------
# printing a perfect square numbers from 1 to 100
# n=1
# while n<=10:
#     print(n**2)
#     n+=1
#----------------------------------------
#searching for number x in this tuple using loop:
# [1,4,16,25,36,49,64,81,100]

# nums=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 16
# i=0
# while i< len(nums):
#     if(nums[i]==x):
#          print("element found at index", i)
#          break
#     else:
#          print("finding .....")
#     i+=1
#---------------------------------------------
#print the elements of the following list using a loop:
# [1,4,16,25,36,49,64,81,100]

# nums=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index=0
# while index < len(nums):
#     print(nums[index])
#     index+=1
#-----------------------------------------
# WAP to find the sum of firdt n numbers 
n = 7
sum = 0
i =1
while i <=n:
    sum+=i
    i+=1
print("total sum :", sum)
#-------------------------------------
# WAP to find the factorial of first n numbers.(using for)
n=5
fact = 1
i = 1
while i <= n:
    fact *=i
    i+=1
print("factorial of n : ", fact)