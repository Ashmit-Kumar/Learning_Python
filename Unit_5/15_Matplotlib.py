import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Matplotlib Line
x=np.array([1,2,3,4,5])
y=np.array([5,6,7,8,9])

# plt.plot(x,y,linestyle='dotted')
# plt.plot(x,y,linestyle='dashed')


# Line Color
# plt.plot(x,y,color='r')

# Line Width
# plt.plot(x,y,lw='20')

# Multiple Line
'''
plt.plot(y,x)
plt.plot([1,2,3,4,5])
'''
x2=[1,2,3,4,5]
y2=[5,4,3,2,1]
plt.plot(x,y,x2,y2) #Multiple line in a same plt.plot()

plt.show()




