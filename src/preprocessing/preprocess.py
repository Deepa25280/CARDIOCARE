import pandas as pd
# Dataset
df=pd.read_csv("data/raw/heart.csv")

print("="* 50)
print("Original Shape")
print(df.shape)

print("=" * 50)
print(df.head)

print("\n missing valus \n")
print(df.isnull().sum())

print("\n Duplicate rows \n")
print(df.duplicated().sum())

df.drop(
    columns=[
        "id",
        "dataset"
    ],
    inplace=True
)
df["target"]=df["num"].apply(
    lambda x:0 if x== 0 else 1

)
df.drop(
    columns=["num"],
    inplace=True
)

import os
os.makedirs(
    "data/processed",
exist_ok=True
)
df.to_csv(
    "data/processed/heart_clean.csv",
    index=False
)
print("Processed dataset saved successfully ")