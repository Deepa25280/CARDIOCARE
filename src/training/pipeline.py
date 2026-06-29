import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split


def create_preprocessor():

    # Numerical columns
    numerical_columns = [
        "age",
        "trestbps",
        "chol",
        "thalch",
        "oldpeak",
        "ca"
    ]

    # Categorical columns
    categorical_columns = [
        "sex",
        "cp",
        "fbs",
        "restecg",
        "exang",
        "slope",
        "thal"
    ]

    # Numerical pipeline
    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    # Categorical pipeline
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    # Combine preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numerical_columns),
            ("cat", categorical_pipeline, categorical_columns)
        ]
    )

    return preprocessor