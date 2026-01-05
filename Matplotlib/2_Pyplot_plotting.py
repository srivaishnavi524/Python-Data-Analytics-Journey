# Pyplot utilies lies under the pyplot submodule, and are usually under the plt alias:
# import matplotlib.pyplot as plt
#now pyplot can be referred as plt.

# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# plt.plot(xpoints, ypoints)
# plt.show()

#the line is drawn from (0, 0) to (6,250)
#------------------------------------------
#plotting x and y points:
# the plot() function is used to draw points(markers) in a diagram

#by default, the plot( ) function will draw a line form point to point.
# parameter 1 -> x-axis, parameter 2-> y-axis

#need to plot a line from (1,3) and (8,10) , we have to pass two arrays [1,8]--> x-axis , [3, 10] --> y-axis

# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([1, 8])
# ypoints = np.array([3,10])
# plt.plot(xpoints, ypoints)
# plt.show()
#  x-axis is a horizontal axis
# y-axis is a vertical axis

#----------------------------------------
#plotting without line : to plot only the marker , we can use a shortcut string notation parameter 'o', which means 'rings' .

# import matplotlib.pyplot as plt
# import numpy as np
# xpoints  = np.array([3 ,6])
# ypoints = np.array([8 , 8])
# plt.plot(xpoints , ypoints , 'o')
# plt.show()

#-----------------------------
# Multiple points : we can plot multiple points , but there should be equal number of elemets in both axis
# draw a line in diagram from position (1, 3) , (3,8), (5, 4) and (7, 8)

# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([1, 3, 5, 7])
# ypoints = np.array([3, 8, 4, 8])
# plt.plot(xpoints, ypoints)
# plt.show()

#-------------------------------------------
# Default X-Points: if we don't specify the x values and we gives only ypoints , then by default x points are start from 0 and 1, 2, 3... etc, depending on the length of y-points
# we cant take default Y pints in this.
#let us take a example for only putting y-axis points 
#No, matplotlib doesn't directly support plotting x values without specifying y.

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([4, 2, 6, 3, 8, 4])
plt.plot(ypoints)
plt.show()

# we can't only give y values but if we want give    plt.plot(xpoints, np.arange(len(xpoints)))  in this way.
