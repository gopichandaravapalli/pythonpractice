import pandas as pd

df=pd.read_json('sample4.json')
print(df)
df.to_csv("CSV.csv",index=False)
result=pd.read_csv("CSV.csv")
print(result)