import pandas as pd
import re 
df=pd.read_csv('Unit_5/Pokemon_data.csv')
print(df.head(3))

# Filtering Data
print(df.loc[df['Type 1']=="Fire"].head(10))

print(df[(df['Type 1']=='Grass')& (df['Type 2']=='Poison')].head(10))

new_df=df[(df['Type 1']=='Grass')& (df['Type 2']=='Poison')]

print(new_df.reset_index())

# Regex
print(df.loc[df['Name'].str.contains('Mega')].head(10))

# Conditional Changes
df.loc[df['Type 1']=='Flamer']='Fire'

df.loc[df['Type 2']=='Fire','Legendary']=True
print(df.head(10))