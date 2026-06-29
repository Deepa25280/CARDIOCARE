import pandas as pd

def load_data():

    df = pd.read_csv("data/processed/heart_clean.csv")

    X = df.drop("target", axis=1)

    y = df["target"]

    return X, y
from src.utils.data_loader import load_data

X, y = load_data()