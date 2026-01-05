# Adding Grid LInes to Plot : 

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115])
# y =np.array([240, 245, 250, 255, 260, 265, 270, 275])
# plt.title("Sports watch Data")
# plt.xlabel("average Pluse")
# plt.ylabel("calories burnage")
# plt.plot(x, y)
# plt.grid()
# plt.show()

#-------------------------------------
# specify which grid line to display 
# we can use axis parameter in the grid() function to specify which grid lines to display

#legal values are x and y. default value is both.

import numpy as np
import matplotlib.pyplot as plt
x = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14,15])
y = np.array([15, 18, 20, 22, 24, 26, 28,29, 30, 33 ])
plt.title("Room Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.plot(x, y)
plt.grid(axis = 'x')  # we can  specify y same as x # plt.grid(axis = 'y')
plt.show()
#-----------------------------------------------------
# Set line properties for the grid 
# grid(color = 'color', linestyle = 'linestyle', linewidth = number) 
#for the above example now set the properties 
plt.grid(color = 'green' , linestyle = '--' , linewidth = 0.5)
plt.show()
