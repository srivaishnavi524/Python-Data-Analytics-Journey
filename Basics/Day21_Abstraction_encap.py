# abstraction
# encapsulation
# del keyword
# private(like) attribute & method
#------------------------------------------
#  Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user. 
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch =True
#         self.acc = True
#         print("car started...")
# car1 = Car()
# car1.start()
#--------------------------------------------
# Encapsulation
#wrapping data and functions into single unit(object).
# class Account:
#     def __init__(self, bal, acc):
#         self.balance =  bal
#         self.account_no = acc
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance = " , self.get_balance())
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance = " , self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account_no)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(10000)
 #-----------------------------------
# del keyword
# used to delete object properties or object itself
# del s1.name # used to del the properties of attributes
# del s1 # used to del the complete obj

# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("hari")
# print(s1.name)
# del s1
# print(s1) # NameError: name 's1' is not defined
#-------------------------------------
# Private(like) attribute & methods
# conceptual implementations in python 
# private attributes & methods are meant to be used only within the class and are not accessible from outside the class
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no= acc_no
#         self.__acc_pass = acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)
# acc1 =Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.__acc_pass)
# # we use __(double underscore) for attributes and methods to declare it as private(or hide the data)
#------------------------------------------
#private methods and attributes
# class person:
#     __name = "anonymous"
#     def __hello(self):
#         print("hello")
#     def welcome(self):
#         self.__hello()
# p1 = person()
# print(p1.welcome())
# print(p1.__name) # error
# print(p1.__hello()) #error