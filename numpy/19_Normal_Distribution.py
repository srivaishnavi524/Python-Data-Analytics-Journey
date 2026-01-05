#the normal distribution is one of the mmost important distribution.
#it is also called Gaussian Distribution
#it fits the probability distribution of many events , eg. IQ scores, Heartbeat etc.
#use random.normal() method to get a normal data distribution..
#it has 3 parameters.

#loc - (Mean) where the peak of the bell exist. ( Like the "average" value where most data points are near)

#scale - (Standard Deviation) Like how "spread out" the data is from the center.how flat the graph distribution should be.

#size - the shape of returned array
#---------------------------------------------
#generate normal random distribution

from numpy import random
x= random.normal(size =(2, 3)) 
print(x)
#---------------------------------------------------
# generating a random normal distribution of size 2x3 with mean at 1, and standard deviation of 2:

from numpy import random
x = random.normal ( loc = 1, scale=2, size=(2, 3))
print(x)
#-----------------------------------------------
# Visualization of  normal distribution

from numpy import random
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot(random.normal(size=1000), kind ='kde')
# plt.show()

#the cureve of a normal distribution is also known as the bell curve because of the bell-shaped curve.
