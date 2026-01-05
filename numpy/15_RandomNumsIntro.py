# What is Random Number?
# Random Number does NOT mean a different number everytime. it means a number we cant predict logically.

from numpy import random 

#generating a random number 0 to 100  -- >  randint()
x = random.randint(100)
print(x)

#generating a floating number using rand()

y = random.rand() # no need to pass any number by default it prints one value, if we pass the that many numbers it will print
#if we dont pass any number it will give direct number , if we pass a number from 1 to any it will give in array formate
print(y)  #that floating number is from n 0 to 1

#generating a random arrays 
arr1 = random.randint(5) # 1-D array
arr2 = random.randint(3, 5) # 2-D array with 3 rows containing 5 random numbers.(rows, columns)

#generating a random number form a array

#choice() method used to generate a random number from the given array.
#it willl take a array as parameter. and return a number form that array

arr3 = random.choice([1, 3, 5, 7, 9])
print(arr3)

#from the given numbers genarate a 2-D array 
arr4 = random.choice([2,4,6,8], size=(3, 5))
print(arr4) # 3 rows containing 5 elements in each 