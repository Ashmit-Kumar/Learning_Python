'''
Why Pandas?
  -Flexibility
  -Working with a very big data
'''

import pandas as pd
import os
df=pd.read_csv('Unit_5/Pokemon_data.csv')
# df1=pd.read_excel('Unit_5/Pokemon_data.xlsx')
df2=pd.read_table('Unit_5/Pokemon_data.txt')
# print(df)
print(df.head(5))
print(df.tail(5))


# Reading data in python
# Read Headers
print(df.columns)

# Read each Columns
print(df.Name)
print(df['Name'])
print(df[['Name','Type 1','HP']])
print(df['Name'].head(10))

# Read each Row

print(df.iloc[1])
print(df.iloc[1:4])
for index,row in df.iterrows():
    print(index,row)
    print(index,row['Name'])
print(df.loc[df['Type 1']=="Fire"])
# To reach specific location
# Syntax df.iloc[r,c]
print(df.iloc[2,1])

# print(f"Current working directory: {os.getcwd()}")