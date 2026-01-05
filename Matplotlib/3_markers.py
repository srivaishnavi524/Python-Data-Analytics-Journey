# Markers: to emphasize the each point with a maker we use this markers. we use marker keyword to use this.

# Marker Reference: 
# 'o' - circle
# '*' - Star
# '.' - Point
# 'x' - X 
# 'X' - X(filled)
# '+' - Plus
# 'P' - pentagon
# 'H'  & 'h' - hexogon
# 's' - Square

#LINE REFERENCE
# '-'  -  Solid line 
# ':'  -  Dotted line 
# '--' - Dashed line
# '-.' - Dashed/dotted line

# COLOR REFERENCE 
# r - red , g - green, b- blue, c-cyan , m- magenta , y - yellow , k - black , w - white
#-----------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 2, 4])
# plt.plot(ypoints, marker = 'o')
# plt.show()
# # mark each ploter with star: 
# plt.plot(ypoints, marker = '*')
# plt.show()

# Formate String fmt : we can also use the shortcut string notation parameter to specify the marker.
# this parameter is also called fmt , and syntax for this is :    marker|line|color
# 1. example

# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([4, 6, 7, 4,7,4])
# ypoints = np.array([4, 8, 3, 7,7,4])
# plt.plot(xpoints, ypoints , '+:g') # + -> marker, : -> line , g -> green 
# plt.show()
#--------------------------------------------
# MARKER SIZE
# we can use keyword markersize or shorter version, ms to set the size of the markers.

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([5, 7, 3, 9])
# plt.plot(ypoints , '*--m' , ms = 10)
# plt.show()
#-------------------------------------------
#MARKER COLOR
#mec , mfc
#keyword markeredgecolor or shorhand 'mec' to set edge color for marker.

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3,6,9,2])
# plt.plot(ypoints, 'D-y' , mec ='hotpink', )
# plt.show()
#------------------------------------------------
#mfc
#markerfacecolor shorthand mfc used to change the inside the edge of the marker 

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([4,5, 2, 6,4 ])
# plt.plot(ypoints, 'H-.m' , mec ='g', mfc='hotpink' , ms=5)
# plt.show()
#-----------------------------------------
#we can use hexadecimal numbers for colors i.e, mec = '#4CAF50', mfc = '#4CAF50'

#marker = 'o,+, *...'
# ms = 5, 10, 20, ....
#fmt = marker|line|color
# mfc ='g'
#mec = 'r'
