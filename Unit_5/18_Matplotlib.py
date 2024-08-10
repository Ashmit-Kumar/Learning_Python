import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Matplotlib Subplot
x=np.random.randint(20,60,30)
y=np.random.randint(20,60,30)
x1=np.random.randint(-10,20,10)
y1=np.random.randint(-10,20,10)
# subplot() : to draw multiple plots in one figure
'''
The subplot() function takes three arguments that describes the layout of the figure.

The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.
''' 

# plot 1
plt.subplot(2,2,1)
plt.plot(x,y)

# plot 2
plt.subplot(2,2,2)
plt.plot(x1,y1)
# plot 3
plt.subplot(2,2,3)
plt.plot(x,y)

# plot 4
plt.subplot(2,2,4)
plt.plot(x,y)
plt.show()


# Ḍraw two function on top of each other

plt.subplot(2,1,1)
plt.grid()
plt.plot(x,y)

plt.subplot(2,1,2)
plt.plot(x1,y1)
plt.show()

# SuperTitle
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP") #super title
plt.show()
