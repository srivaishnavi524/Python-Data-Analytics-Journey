#we cannot directly use abstract classes and abstract methods in python but we have a module ABC module(Abstract Base Classes)

#Abstract Methods: the method which has only declaration but not defination we call it as Abstract Method.
# Abstract  class: 
# --to make a class as abstract we should import ABC and abstractmethod from abc
# --when we make a class as abstract class we cant create a object for it
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        print("Running")

class Laptop(Computer):
    def process(self):
        print(" Its Runninggg") 

class Whiteboard:
    def write(self):
        print("its writing")

class Programmer:
    def work(self, com):
        print("solving Bugs")
        com.process()

com1 = Laptop()
prog1 = Programmer()
prog1.work(com1)
com1.process()

#abstract class should have atleast one abstract method
#---------------------------------------------------------
