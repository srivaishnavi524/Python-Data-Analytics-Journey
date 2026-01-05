# Display Multiple Plots
# with subplot(  ) function we can draw multiple plots in one figure.
#DRAW 2 PLOTS

# import matplotlib.pyplot as plt
# import numpy as np

# #plot 1
# x = np.array([0, 1, 2, 3, 4])
# y = np.array([3, 8, 5, 4, 6])
# plt.subplot(1, 2, 1) # 1 row, 2 columns , 1st place
# plt.plot(x, y)

# #plot 2
# x1 = np.array([0, 1, 2, 3, 4])
# y1 = np.array([4,2,6,3,8])
# plt.subplot(1, 2, 2) #1 row, 2 columns, 2nd place
# plt.plot(x1, y1)

# plt.show()
#----------------------------------------------
# subplot() function takes 3 arguments that discribe the layout of the graph.
#rows, columns , and places where they are occupied.
# draw 2 plots on top of each other.
#title()  function : we can add title to each plot with title()
#suptitle() : we can add titel to entire figure 

import matplotlib.pyplot as plt
import numpy as np

#plot 1
x = np.array([1, 3, 4, 8])
y = np.array([2, 4, 6, 8])
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title("Income")

#plot 2
x =np.array([0,1, 2, 3])
y = np.array([4, 6, 3,10])
plt.subplot(2, 1, 2)
plt.plot(x, y)
plt.title("Sales")

plt.suptitle("Business")
plt.show()
#-------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()