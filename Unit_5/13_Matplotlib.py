import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xpoints=np.array([0,6])
ypoints=np.array([0,250])
xy=np.array([[0,6],[0,250]])
# plt.plot(xpoints,ypoints)
# plt.plot(xy[0],xy[1])
# plt.show()



# Plotting x and y points in a line
# plt.plot(xpoints,ypoints)

# to plot points 
x=np.array([[1,2,3,4,5,6],[6,5,4,3,2,1]])
# plt.plot(xpoints,ypoints,'o')
# plt.plot(x[0],x[1],'o')
plt.show()


# Default X-points: If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
plt.plot([1,3,2,5,4])
# plt.plot([1,3,2,5,4],'o')
plt.show()