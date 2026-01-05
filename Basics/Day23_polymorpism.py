# POLYMORPHISM : 
#  OPERATOR OVERLOADING
# When the same operator is allowed to have different meaning according to the context

# operators & dunder functions
# addition  a + b     a.__add__(b)
# a.__sub__(b)   a.__mul____(b)   a.__truediv____(b)   a.__mod____(b) 
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img, "j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)
        
# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 6)
# num2.showNumber()

# num3 = num1+num2
# num3.showNumber()
#--------------------------------------------
# example 1
# Define a circle class to create a circle with radius r using the constructor. 
# define an Area() method of class which calculates the area of the circle.
# define a perimeter() method of the class which allows you to calculate the perimeter of the circle
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def Area(self):
#         return 22/7 * self.radius **2
    
#     def perimeter(self):
#         return 2* 22/7 * self.radius
    
# c1 = Circle(21)
# print(c1.Area())
# print(c1.perimeter())

#example 2
# Define a employee classnwith attribute role, department & salary. this class also has a showDetails() method.
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role = ", self.role)
#         print("dept = ", self.dept)
#         print("salary = ", self.salary)

# e1 = Employee("accountant", "Finance", "60,000")
# e1.showDetails()
#--------------------------------------
# create an engineer class that inherits properties from employee &  has additional attributes : name & age

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "100000")
# Engg1 = Engineer("krish", "30")
# Engg1.showDetails()
#-----------------------------------------------
# Create a class called order which stores item & its price. 
# use Dunder function __gt__() to convey that:
#  order1 > order2 if price of order1 > price of order 2
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, odr2):
#         return self.price > odr2.price

# odr1 = Order("idli", 60)
# odr2 = Order("dosa", 50)

# print(odr1 > odr2)
#-----------------------------------------------
# 4 ways of implementing polymorpism
# Duck typing
# Operator overloading
# method overloading
# method overriding
#------------------------------
# Duck typing
# class PyCharm:
#     def execute(self):
#         print("compiling")
#         print("Running")

# class MyEditor:
#    def exectute(self):
#       print("spell check")
#       print("Convention Check")

# class Laptop:
#   def code(self, ide):
#      ide.execute() # we can take any name not only ide , but we should pass that name only in the code
     
# ide = PyCharm() # or ide  = MyEditor
# lap1 = Laptop()
# lap1.code(ide)

# here we can take any class which contains the execute method in it , we can consider that 
#  if there is a bird that behaves like duck, walks like a bird, swim like a bird , quacks like a duck then it should be a duck, in the same way which is an obj which is a ide and it has method execute then its enough, we are not consern about which class obj it is.
#-----------------------------------------------
# OPERATOR OVERLOADING
# Synthetic Sugar : ?
# a = 5
# b =6
# print(a + b)
# print(int.__add__(a,b)) # o/p is 11
# c = "5"
# d = "6"
# print(str.__add__(c,d)) #o/p is 5 6
#-----------------------------------------
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2

#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)
#         return s3

#     def __gt__(self,other):
#         r1 =  self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         if r1 > r2:
#             return True
#         else:
#             return False
        
# s1 = Student(58, 69)
# s2 = Student(60,65)
# s3 = s1 + s2
# print(s3.m1)
# if s1 > s2 :
#     print("s1 wins")
# else:
#     print("s2 wins")
#------------------------------------------------
# METHOD OVERLOADING:
# In a class if we have same method name with different parameters . but in python we cannot create 2 methods whit same name.
#METHOD OVERRIDING
#same method name and same parameters in different class (inheritance)
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2

#     def sum(self, a, b): # sum(self, a =None, b=None) -> by default we can write like this 
#         s = a + b
#         return s
#     def sum1(self, a, b,c=None): # sum(self, a =None, b=None) -> by default we can write like this 
#         r = 0
#         if a!=None and b!= None and c!= None:
#             r = a + b + c
#         elif a!= None and b !=None:
#             r = a + b
#         else:
#             r = a
#         return r
        
# s1 = Student(58, 69)
# print(s1.sum(6, 7))
# print(s1.sum1(4,5)) #whichout c value also we can execute 
#----------------------------------------------
# METHOD OVERRIDING
class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        # pass  # it prints the A clss stmts
        print("in B show") 

a1 = B()
a1.show()
