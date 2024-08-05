import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4])
y=np.array([4,3,2,5])

# plt.bar(x,y)
# The default width value of a bar is 0.8
# plt.bar(x,y,color='r',width=0.1)
plt.bar(x,y,height=0.3)

# horizontal bar
# plt.barh(x,y)
plt.show()


