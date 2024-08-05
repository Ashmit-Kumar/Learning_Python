import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Basic Graph
# plt.plot([1,2,3],[4,5,6])
x=[1,2,3]
y=[6,7,8]
plt.plot(x,y)# this can give decimal value to so if you want only integer in x and y axis
plt.xticks(x)
plt.yticks(y)

plt.title("Our First Graph",fontdict={'fontname':'Comic Sans MS','fontsize':20}) # to give title
# you can add fontdict to x and y labels also
# xlabel
plt.xlabel("our x axis")

# y label
plt.ylabel("our y axis")
plt.show()
