# pass 
# if-elif-else(syntax)
# if(condition):
#     Stmt1
# elif(condition):
#     Stmt2
# else:      
#     Stmt..N  
#-------------------------------------------
# age=21
# if(age>=18): #true 
#     print("eligible for driving") #indentation (4 spaces/ tab space)
#     print("they can vote")
#------------------------------------------
# light ="Green"
# if(light=="Red"):
#     print("stop")
# elif(light=="Green")    :
#     print("Go")
# elif(light=="Yellow"):
#     print("Get Ready")    
# else:
#     pass   # if no print stmts are written then we need to write pass , so that it don't show any error
# #     print("Your Wish")   
# print("End of Driving Time . Take rest")
#--------------------------------------------
# num=5
# if(num >20):
#     print("num is greater than 20")
# if(num>3):
#     print(" num greater that 3") # only this stmt is executed
#----------------------------------------------
# grade students based on marks 

# marks=int(input("enter student marks: "))
# if(marks>=90):
#     print("A grade")
# elif(marks<90 and marks>=80):
#     print("B grade")
# elif(marks<80 and marks>=70):
#     print("C grade")
# else:
#     print("D grade")
#----------------------------------------
# nested if-else stmts
#-----------------------------------------
# age =90 # age should be greater that 34 and less than 70 for driving

# if(age>=18):
#     if(age>70):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     ("cannot drive")
#--------------------------------------------
# example1(even or odd)
# num=int(input("enter a number: "))
# if(num%2==0):
#     print(num,"is even number: ")
# else:
#     print(num,"is odd number: ")
#-----------------------------------------------
#example2(greatest of 3 entered by user)
# num1=int(input("enter 1st number: "))
# num2=int(input("enter 2nd number: "))
# num3=int(input("enter 3rd number: "))
# if(num1>=num2 and num1>=num3):
#     print(num1,"is greatest ")
# elif(num2>=num3):
#     print(num2,"is greatest")
# else:
#     print(num3,"is greatest")
#---------------------------------------------
#example3(check if num is multiple of 7 or not)
# number=int(input("enter a number: "))
# if(number%7==0):
#     print(number,"is multiple of 7")
# else:
#     print(number,"is not multiple of 7")
#-----------------------------------------------
# example4(prime or not)
# 1st method
# num = 7
# for i in range(2,num):
#     if num % i == 0:
#         print("not a prime") #if num = 6 find 6 % (1,2,3,4,5) should not eqal to 0 , if it is eqal to 0  then that num is divisible to another numbers other than 1 And itself
# else:
#     print("is a prime")# 7 % (1,2,3,4,5,6) any of this nums is not equal to 0 
# 2nd method(sqrt)