import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=np.random.randint(10,20,10)
y=np.random.randint(10,20,10)

# Add Grid lines to plot
plt.plot(x,y)
plt.title("Graph")
plt.xlabel("X-axis")
plt.ylabel('Y-axis')
# plt.grid() #display grid in both x and y axis
# plt.grid(axis='x') #display grid in  x  axis only
# plt.grid(axis='y') #displays grid in y axis only

plt.grid(ls=':')
plt.show()