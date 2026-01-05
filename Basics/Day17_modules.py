# A Python module is a single file containing Python code (functions, classes, and variables) that serves as an organizational and reusable unit in a program. Any Python file saved with a .py extension is essentially a module. 

# for reusing  file we will import them to another file where we want to use that functions or classes
#------------------
# type 1
import Day17_a 
c = Day17_a.add(4,5)
print(c)
#---------------------
#type 2
# from Day17_a import add # from module a if we want only add module we should specify that module
# from Day17_a import * # will import all the functions
