# data distribution is a list of all posible values and how often each value occor.
#such list are important when working with statistics and data science
#random Disrubtion: probability function
from numpy import random
# generate 1-D array with 100 values where values has to be 4, 6, 8, 2
# the probability of the value 4 is set to be 0.5
#the probability of the value 6 is set to be 0.0
#the probability of the value 8 is set to be 0.1
#the probability of the value 2 is set to be 0.4
# the probability is set by a number 0 to 1 , where 0 means never occor and 1 means always occur.
#the sum of all possible outcomes should be 1
# arr1 = random.choice([2, 4, 6, 8], p =[0.4, 0.5 , 0.0, 0.1], size=(100))
# print(arr1)

#same example with generating 2-D array, with 3 rows and 4 colums 

arr2 = random.choice([2, 4, 6, 8], p =[0.4, 0.5 , 0.0, 0.1], size=(3,4))
print(arr2) # 2-D array 3 sub arrays with 4 elements in each
