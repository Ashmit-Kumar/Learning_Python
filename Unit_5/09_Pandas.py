import pandas as pd

df=pd.read_csv('Unit_5/Pokemon_data.csv')

# Sorting/Describing Data
print(df.describe())

# Ascending Order Sorting
print(df.sort_values('Name').head(10))
print(df.sort_values(['Name','HP']).head(10))

# descending Order Sorting
print(df.sort_values('Name', ascending=False).head(10))


# Make changes to  a data
df['Total']=df['HP']+df['Attack']
print(df['Total'])
df=df.drop(columns=['Total'])
print(df.head(5))
df['Total']=df.iloc[:,4:10].sum(axis=1)
print(df.Total.head(3))

# Rearranging columns order
cols=df.columns.values
# df=df[['Total','HP','Defence']]

# Saving the new CSV

df.to_csv('Unit_5/modified_data.csv')
df.to_csv('Unit_5/modified_data_1.csv',index=False)

