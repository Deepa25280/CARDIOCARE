import pandas as pd
df = pd.read_csv("data/heart.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info)