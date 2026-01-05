# Variables : Variables are containers for storing data values, orr variable is the name given to a memory location in a program
x =5  # x is a variable 
# variables do not need to be declared with any particular type,and can even change type after they have set
# x = 5        >> x is a int type 
#x =" hello"  >>  x is now string type
#-------------------------------------
# casting: If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#-------------------------------------
#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))   # x is int type 
print(type(y))   # y is string type 
# variable are case-sensitive
#-------------------------------------
# Rules for Python variables:

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.
#-------------------------------------
#Camel Case :Each word, except the first, starts with a capital letter:  myVariableName = "John"

#Pascal Case :Each word starts with a capital letter: MyVariableName = "John"

#Snake Case: Each word is separated by an underscore character: my_variable_name = "John"
#-------------------------------------
#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#-------------------------------------
#Unpack a Collection  :If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)    #Python is awesome ("  , " is used to give spaces for the given string)
#-------------------------------------
# global variables can be used inside and ouside of the function , where as local variables can be used only inside the function 
# we can declare a global variable in side a function using global 
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)  #python is fantastic
#--------------------------------
 