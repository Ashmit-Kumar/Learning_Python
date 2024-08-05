import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Labels and Titles
x=np.random.randint(1,20,10)
y=np.random.randint(1,20,10)
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

# xlabel()
# plt.xlabel("X-axis")
plt.xlabel("X-axis",fontdict=font1)

# ylabel()
# plt.ylabel("Y-axis")
plt.ylabel("Y-axis",fontdict=font2)

# Title of the graph
plt.title("Graph")

plt.plot(x,y)
plt.show()
