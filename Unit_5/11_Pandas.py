import pandas as pd 

df=pd.read_csv('Unit_5/Pokemon_data.csv')

print(df.groupby(['Type 1']).mean(numeric_only=True).sort_values('Attack',ascending=False))

print(df.groupby(['Type 1']).sum())
print(df.groupby(['Type 1']).count())
print("end")
print("code")

