#if we want to display bars horizontally use barh() function

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

#------------------------------------
# bar() and barh() take the keyword argument color to set the color of the bars.

#  import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "red")
# plt.show()
#-----------------------------------------
# color name : 140 supported color names or we can use hexadecimal values
#------------------------------------------
# Bar Width: The bar() takes the keyword argument width to set the width of the bars:
plt.bar(x, y, width = 0.1)
#-----------------------------------------
# Bar Height:The barh() takes the keyword argument height to set the height of the bars.
#Note: For horizontal bars, use height instead of width.

plt.barh(x, y, height = 0.1)
#--------------------------------------------