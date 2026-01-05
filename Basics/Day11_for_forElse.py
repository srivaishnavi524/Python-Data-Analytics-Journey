# range 
# print the following list using loop
# nums=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in nums:
#     print(el)
#-------------------------------------
# search for a number x in this tuple using for loop
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# nums=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x=25
# index=0
# for el in nums:
#     if (el == x):
#         print("element found at index: ", index)
#         break
#     index+=1     
#-------------------------------------
#even nums 1 to 10
# for i in range(2, 12, 2):
#     print(i)
#-------------------------------------
#range(start ?, stop, step?)
# start is optional , by default 1
# step is also optional , default 1
#stop mandatory
  #-------------------------------------
# pass is a null statement that does nothing.it is used as a placeholder for future code 
# for el in range(10):
#     # pass # if we comment this pass then it shows error in the code because for loop doesnot providing any stmts 
# having an empty for loop like this, would raise an error without the pass statement
# print("hy")
#-------------------------------------
# seq=range(5)
# for i in seq:
#     print(i) #0 to 4
#-------------------------------------
# WAP to find the sum of firdt n numbers 
# n=5
# sum=0
# for i in range(1, n+1):
#     sum +=i
# print("total sum : " , sum)
#-------------------------------------
# WAP to find the factorial of first n numbers.(using for)
# n=5
# fact=1
# for i in range(1,n+1): # if we take upto n then n is not included so we should take n+1 
#     fact*=i
# print("factorial = ",fact)
#-------------------------------
# for-else loop:  
nums =[12,33,2,28,18,3]
for num in nums:
    if num % 5 ==0:
        print(num)
        break
else:
    print("not found")
        