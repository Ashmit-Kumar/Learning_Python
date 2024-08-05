import matplotlib.pyplot as plt
import numpy as np


# Creating Scatter Plots
'''
With Pyplot, you can use the scatter() function to draw a scatter plot.

The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:
'''

x=np.random.randint(10,20,10)
y=np.random.randint(10,20,10)
x1=np.random.randint(0,20,10)
y1=np.random.randint(0,20,10)
x2=np.random.randint(5,25,15)
y2=np.random.randint(5,25,15)
# plt.scatter(x,y)
# plt.scatter(x1,y1)
plt.scatter(x,y,color='r')
# plt.scatter(x1,y1,color='b')
plt.scatter(x1,y1,color='b',s=[30],alpha=0.5)
# alpha: transparency
plt.colorbar()
plt.show()