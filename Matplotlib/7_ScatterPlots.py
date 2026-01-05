# with pyplot , we can use scatter( )function , to draw scatter plots.
#scatter() function plots for each observation. it also need two array of same length, one for x axis and other for y axis.
#--------------------------------------------
#simple scatter plot
# import matplotlib.pyplot as plt
# import numpy as np
# x =np.array([1,2, 3, 4, 5])
# y = np.array([2, 5, 7, 6, 8])
# plt.scatter(x, y)
# plt.show()
# # the above example plots 4 observations
#-----------------------------------
#comparing plots 
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1,4, 6, 9, 10, 14])
# y =np.array([18, 17, 15, 14, 11, 8])
# plt.scatter(x,y)

# x=np.array([8, 10, 12, 14, 16])
# y =np.array([18, 22, 26, 27, 30 ])
# plt.scatter(x, y)

# plt.show()
#by default the blue and orange colors will be there 
# #----------------------------------------
# changing colors : 
# plt.scatter(x, y, color = "green")
# plt.scatter(x, y, color = "#88c999")
#-------------------------------------------
# Color each dot.
# we can specify the different colors to each dot using array of colors as value fot the c argument.
# note: we cannot use color as argument, we can use c as argument.
#---------------------------------------------
#set different colors to the dots 
# import matplotlib.pyplot as plt
# import numpy as np

# x= np.array([1,2,3,4,5])
# y =np.array([1,2,3,4,5])
# colors = np.array(["red", "blue","orange", "green", "pink"])
# plt.scatter(x, y, c = colors) # we should pass only c for colors, no other arguments.
# plt.show()
#----------------------------------------------
#ColorMap: colormap is a list of colors , each color ranges from 0 to 100.
#color map ranges from 0 (purple) upto 100(yellow).. viridis
#HOW TO USE COLORMAP :
#we can specify with the keyword argument cmap with value of color map. 
# 'viridis' which is one of the built-in colormaps available in matplotlib
# Create a color array, and specify a colormap in the scatter plot:

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([5,7,8,7,2,17,2])
# y = np.array([99,86,87,88,111,86,103])
# colors = np.array([0, 10, 20, 30, 40, 90, 100])
# plt.scatter(x, y, c=colors, cmap='viridis') # cmap ='nipy_spectral'
##we can include colorbar() into the graph (optional)
# plt.show()
#----------------------------------------------
#SIZE : we can change the size of dots with s arguments.
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# plt.scatter(x, y, s=sizes)
# plt.scatter(x, y, s =20) #also correct
#-----------------------------------------------------
# Alpha : we can adjust the transparency of the dots with the alpha argument.
# plt.scatter(x, y, s=sizes, alpha=0.5)
#----------------------------------------------
# we can conbine size and alpha together

import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2])
y = np.array([99,86,87,88,111,86,103])
sizes = np.array([80, 90, 105, 90, 125, 60, 70])
colors = np.array([0, 10, 20, 30, 40, 90, 100])
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='nipy_spectral')
plt.colorbar()
plt.show()