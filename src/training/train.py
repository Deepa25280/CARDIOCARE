import pandas as pd

df=pd.read_csv("data/processed/heart_clean.csv")

print(df.head())
print(df.shape)

x=df.drop("target",axis=1)
y=df["target"]

print("Feature Shape :",x.shape)
print("Target shape :",y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
print("\nTraining Data")
print(X_train.shape)

print("\nTesting Data")
print(X_test.shape)