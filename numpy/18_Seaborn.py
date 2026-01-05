#matplotlib(pyplot) - seaborn 
#seaborn is a library that uses matplotlin underneath to plot graph i.e pyplot
""" 
#Distplot - distribution plot(curve plot - histogram)
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5])
plt.show()

#distplot is a old version so better to use displot() `distplot` is a deprecated function and will be removed in seaborn v0.14.0.

# Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
"""
# Displots: displot stands for distribution plot, it takes an input array and plot a curve corresponding to the distribution of points in the array

#plotting a Displot:
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot([0, 1, 2, 3, 4, 5])
plt.show() # shows the ploting numbers
#plotting a Displot without the histogram
# sns.displot([0, 1, 2, 3, 4, 5, 6], kind = "kde")
plt.show()

#note: we will be using : sns.displot(arr, kind ="kde") to visualize random distribution 