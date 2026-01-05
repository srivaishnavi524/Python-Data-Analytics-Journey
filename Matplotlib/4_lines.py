# Linestyle: can also written as ls

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'dotted') 
# # plt.plot(ypoints, ls = 'dotted')  # we can write in way also
# plt.show()
#-------------------------------------------
# linestyle can be written as ls
# dotted can be written as :
# dashed can be written as --
# 'solid' (default)   as 	'-'
# 'dashdot'	'-.'	
# 'None'	'' or ' ' # plane graph 
#--------------------------------------
#line color :set color for line
# color or c (shorthand)
#we can use hexadecimal values for colors ex.  c = '#4CAF50' or colornames ex. c = 'hotpink'
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, color = 'r') # color or c ='r'
# plt.show()
#------------------------------------------
# linewidth:  linewidth or the shorter lw

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linewidth = '20.5') # we can give integer values also
# plt.show()
#--------------------------------------------
#multiple lines : 
# import matplotlib.pyplot as plt
# import numpy as np
# y1 = np.array([3, 6, 9, 10])
# y2 = np.array([5, 2, 4, 6])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()
#----------------------------------------------
#we can use x-axis and y-axis plots for multiple lines 

import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1)
plt.plot(x2, y2) # we can write like this also plt.plot(x1, y1, x2, y2)
plt.show()
#----------------------------------------------
