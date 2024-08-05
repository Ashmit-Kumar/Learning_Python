import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Histogram

x=np.random.randint(10,30,15)
y=np.random.randint(10,30,15)

plt.hist(x)
plt.show()