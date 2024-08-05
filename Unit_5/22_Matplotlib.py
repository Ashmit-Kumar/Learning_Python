import matplotlib.pyplot as plt
import numpy as np

# Pie
y=np.array([35,35,15,5,10])
lab=np.array(['A','B','C','D','E'])
explode=[0.2,0,0,0,0]
print(y.sum())
# plt.pie(y)
# plt.pie(y,labels=lab)
# Startangle
# plt.pie(y,labels=lab,startangle=90)
# explode: to make a edge standout
# plt.pie(y,labels=lab,explode=explode)

# Shadow
plt.pie(y,labels=lab,explode=explode,shadow=True)

# Legend Function
# plt.legend()
# Legend with header
plt.legend(title="Hello")


plt.show()
