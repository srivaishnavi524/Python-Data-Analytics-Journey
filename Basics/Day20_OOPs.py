# __init__(constructor)(2 types)
# Class and Instance Attributes()
# methods
#instance methods(self)
# static methods (static)

#-----------------------------------
# OOP in python 
# - to map with real world scenarios, we started using objects in code
# - this is called object oriented programming
# use of functions -> redundancy decresed, reusability increased
# procedural -> functional programming -> object oriented programming
# CLASS & OBJECT IN PYTHON
# print("hello", end=" ")
# class Student:
#     name = "kiran"

# s1 = Student()
# print(s1.name)
#-------------------------------------
# class car:
#     color = "blue"

# car1 = car()
# print(car1.color)
#-------------------------------------
# accessing the values and functions from the class
# class person:
#     name  = "kiran"
#     age = 12
#     def marks(self):
#         math = 20
#         science = 19
#         print(math)
# obj1 = person()  #creating object for class person
# person.marks(obj1) # we can call method i this way too
# print(obj1.name) #accessing the name in class
# obj1.marks() # accessing marks from the function
# print(obj1.age) # accessing the age from the class age
#--------------------------------------
# __init__ function :
# inti is a constructor
# all classes have a function called __init__(), which is always executed when the object is being initiated. __init__ method is called automatically for every object is created.(1 obj one time call, 2 obj's 2 tym calls)
# when evern we create a class it always has a constructor. if we dont write the constructor in the code python will automatically create one for us.if we need our own costructor we can create it.
# a constructor is bacically for initializing An object. ie, if we want to perform some operation we create it and perform operations in that constructor.
#2 types of constructors (default, parameterized). the 1st parameter is always the self (object instance itself)
#  # creating clss
# class Student:
#     def __inti__ (self, fullname): 
#         self.name = fullname 

# #creating object
# s1 = Student("karan")
# print(s1.name)


#--------------------------------------
# class Mobile:
#     def __init__(self,Brand,Battery,Ram,Camera,Price):
#         self.Brand = Brand
#         self.Battery = Battery
#         self.Ram = Ram
#         self.Camera = Camera
#         self.Price = Price
#     def display(self):
#         print("Brand :", self.Brand) # self allows the another method's values to this method within same class
#         print("Battery :", self.Battery)
#         print("Ram:",self.Ram)
#         print("Camera :",self.Camera)
#         print("Price :", self.Price)
# obj = Mobile("apple","48mah", "6GB","5000MP", "90000") # if we want to disply same mobile object for 5 times use for loop above obj
# obj.display()
# obj1 = Mobile("Samsung S24","5000mah", "6GB","50MP", "90000") 
# obj1.display() # we can create multiple objects for a single class
# print(obj1.Brand , obj1.Price)  # it prits the brand name and price
# the self paramater is a reference to the current instance of the class, and is used to access variables that belongs to the class.(self is reference of the object)
#-----------------------------------------
# class Car:
#     def __init__(self):
#         print("this is init")
#     def BMW(self):
#         print("this is car")
# obj = Car()
# obj.BMW() #init method is called by default  when we create object but we should call the other methods 
#--------------------------------------
#parameterized constructor
# class Student:
#     name ="unknown"  # class Attribute
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks # method attribute
#         print("adding the new student details to DB..")
# s1 =Student("kiran", 97)
# print(s1.name, s1.marks) # here name kiran will print , because obj attr > class attribute (object precedence has higher priority)
#-------------------------------------------
# Class & Instance Attributes
# we call variables as attributes in OOPs, functions as methods 
# Class.attr
# obj.attr
#above example
#ACCESSORS(for accessing the value) & MUTATORS(for modifying the value)

# class Student:
#     school = "Con"
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3
    
#     def get_m1(self):
#         return self.m1 

#     def set_m1(self, value):
#         self.m1 = value

# s1 = Student(34, 55, 44)

# print(s1.avg())

 #------------------------------------------
# Methods : Methods are functions that belongs to objects. 
#------------------------------------------
# Example 1: create student class that takes name & marks of 3 subjects as arguments in constructor. then create a method to print the average. 
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks 
#     def get_avg(self):
#         sum =0
#         for val in self.marks:
#             sum += val
#         print("hii", self.name, "your avg score is : ", sum/3)
# s1= Student("ram",[20, 19, 18])
# s1.get_avg()
#------------------------------------------------
# Static Methods
#  methods that dont use the self paramenter(work at class level)
# class books:
#     @staticmethod   #decorator
#     def textbooks():
#         print("textbooks")
#     def notebooks(self):
#         print("notebooks")
#     def __init__(self):
#         print("roughbooks") # no need to call the constructor , it automatically call them 1st
# b1 =books()
# b1.textbooks()
# b1.notebooks()
 #decorator allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
 #-------------------------------------------

