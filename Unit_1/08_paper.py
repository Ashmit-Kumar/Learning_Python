import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('cites.csv')
# print(df)

last_column=df.iloc[:,-1].values
df=df.iloc[:,:-1]
# print(df)
s=df.iloc[:,-1].values
# print(s)
x=df.columns[0]
print(x)

plt.scatter(df.iloc[:,0],df.iloc[:,1],c='blue')
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.title("plot ")
plt.grid()
plt.show()