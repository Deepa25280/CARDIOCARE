import pandas as pd
df = pd.read_csv("data/processed/heart_clean.csv")

categorical_columns =[
    "sex",
    "cp",
    "fbs",
    "restecg",
    "exang",
    "slope",
    "thal"
]
for column in categorical_columns:
    print("=" * 60)
    print(column.upper())
    print(df[column].unique())