# inheritance(types)
# super method
# class method (class)
#polymorpism
#-----------------------------------------
#inheritance
# when one class(child/derived) drives the properties & methods of another class(parent/base) 
#parent class
# class Car:
#     @staticmethod
#     def start():
#         print("car started....buuyiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    
#     @staticmethod
#     def stop():
#         print("car stopped..")

# # child class  
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
#         print("how is riding expirence")

# car1 = ToyotaCar("prius")  

# # now using parent class properties
# car1.start() # it prints the statements from the start menthod which is there in the parent class 
# #------------upto here single level inheritence----------
# class BMW(ToyotaCar):
#     def __init__(self, brand):
#         self.type = type
#         print("car mileage of this car is 20km ")
# car2 = BMW("diesel")
# car2.stop()
#------------------this is multilevel inheritence-----------------
# OUTPUT
# how is riding expirence
# car started....buuyiiiiiiiiiiiiiiiiiiiiiiiiiiiii
# car mileage of this car is 20km 
# car stopped..

#----------------------------------------------
#types of inheritance in python
# 1. Single Ievel Inheritance   (base-> derived)
# 2. Multi- level Inheritance (base1-> base2-derived1 ->derived)
# 3. Multiple Inheritance(from base 1 and base2 -> derived class)

# above code is the example for single and multi-level inheritance
#MULTIPLE INHERITANCE
# from base 1 and base2 -> derived class
# class A:
#     varA ="welcome to class A"
# class B:
#     varB = "welcome to class B"
# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)
#-------------------------------------------
# Super Method
# super()method is used to access  methods of the parent class 
# class Car:
#         def __init__(self, type):
#                 self.type = type
#         @staticmethod
#         def start():
#             print("car started ...")
        
#         @staticmethod
#         def stop():
#             print("car stopped..")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         self.type = type
#         super().start()
#        # inside the super/parent class methods select one method , we selected constructor method and type method
         

# car1 = ToyotaCar("prius", "electric")
# print(car1.type) # car1 obj is toyotacar and that car type is electric
#-----------------------------------------------------
# METHOD RESOULTION ORDER (LEFT TO RIGHT)
# -> If we are inheriting properties from class A and Class B to class C through __init__ method , using super keyword . this super keyword only takes the properties only from class A even class B also have __init__ method 
# -------------------------------------------------
# Class Method
# A class method is bound to the class & receives the class as an implicit first argument
# class Student:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Student()
# p1.changeName("rahul kumar")
# print(p1.name)    # it prints rahul kumar
# print(Student.name) # here in class name attr anonymous changes to rahul kumar
#-----------------------------------------
# Property decorators: we use @property decorator on any method in class to use the method as a property(it can be accessed like an attributes)
#benifit: Add additional logic when read, write or delete attributes gives you getter(read), setter(write), and deleter(delete) method
# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height

#     @property
#     def width(self):
#         return f"{self.__width:.1f}cm"
#     @property
#     def height(self):
#         return f"{self.__height:.2f}cm"

# rectangle = Rectangle(3, 4)
# print(rectangle.width)
# print(rectangle.height)
#------------------------------------------------------
