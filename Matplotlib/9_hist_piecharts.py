# Matplotlib Histograms: A  histogram is a graph showing frequency distributions.
#this graph shows the number of observations within each intervel of time.
# we need 250 values , where the values will concentrate around 170, and standrad deviation is 10. 

# import matplotlib.pyplot as plt
# import numpy as np
# x =np.random.normal(170, 10, 250) # generate 250 values , average 170 values,mostly numbers are in between 160 ro 180  i.e, 170+- 10.

#---------------------------------------------
# hist() function will read the array and produce a histogram
 
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.normal(170, 10, 250)
# plt.hist(x)
# plt.show()

#----------------------------------------------
# creating pie charts
#with pyplots we can use pie() function to draw pie charts.
# by default the plottting of 1st wedge starts from x-axis and moves counterclockwise.
# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# plt.pie(y)
# plt.show() # starts from blue

# note: the size of each wedge is determined by comparing the value with all other values, by using formula: the value divided by sum of all values: x/sum(x)
#-----------------------------------------
# Adding lables to the pie chart

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylables = ['apple', 'banana','orange', 'mango']
# plt.pie(y, labels= mylables)
# plt.show()
#-------------------------------------------
# Start Angle: default start is at x-axis , but we can change the start angle by specifying startangle parameter in pie 

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels =["apples", "banana", "orange", "Mangoo"]
# plt.pie( y, labels = mylabels , startangle =90)
# plt.show()
#----------------------------------------------
# Explode: in chart one of the wedges to standout, we use explode parameter
#each value represent how far from the center each wedge is displayed.

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([35, 25, 25, 15])
# mylabels = ['apple', 'banana', 'orange', 'mango']
# myexplode = [0.2, 0, 0.1, 0] #1st wedge i.e, apple will move out of the chart
# plt.pie(x, labels =mylabels, explode = myexplode)
# plt.show()
#----------------------------------------------
#Shadow : add shadow to pic by setting  (shadow = True) parameter to apper the shadow to the chart
# plt.pie(x, labels =mylabels , explode=myexplode, shadow=True)
#----------------------------------------------
# colors: we can set colors to wedges by passing colors parameter.
# if colors parameter is specifies , there should be an array with one value for each wedge.
#we can have hexadecimal values or shorcuts  for r-red, g-gree, b-blue, c-cyan, m-megenta, y-yellow, k-black, w-white

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([25, 35, 25, 15])
# mylabels= ['apple', 'banana', 'orange', 'mango']
# mycolors = ['c', 'yellow', '#4CAF50', 'hotpink']
# plt.pie(x, labels =mylabels, colors = mycolors)
# plt.show()

#----------------------------------------------
# Legend: to add list of explanation about the chart 

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([25, 35, 25, 15])
# mylabels= ['apple', 'banana', 'orange', 'mango']
# mycolors = ['c', 'yellow', '#4CAF50', 'hotpink']
# plt.pie(x, labels =mylabels, colors = mycolors)
# # plt.legend()
# plt.legend(title ="fruits") #adding title to the legend
# plt.show()
#------------------------------------------------
# Legend with Header
# we can add title for the legend by passing the title parameter to legend
# plt.legend(title ="fruits")