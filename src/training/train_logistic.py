import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#load dataset

df=pd.read_csv("data/processed/heart_clean.csv")

#feature and target
x=df.drop("target",axis=1)
y=df["target"]

#numerical column
numerical_columns = [
    "age",
    "trestbps",
    "chol",
    "thalch",
    "oldpeak",
    "ca"
]
#categorical column
categorical_columns = [
    "sex",
    "cp",
    "fbs",
    "restecg",
    "exang",
    "slope",
    "thal"
]
#numerical pipeline
numeric_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        ),

        (
            "scaler",
            StandardScaler()
        )
    ]
)
#categorical pipeline
categorical_pipeline = Pipeline(
    steps=[

        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),

        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore")
        )

    ]
)
#preprocessor
preprocessor = ColumnTransformer(

    transformers=[

        (
            "num",
            numeric_pipeline,
            numerical_columns
        ),

        (
            "cat",
            categorical_pipeline,
            categorical_columns
        )

    ]

)

#complete ML Pipeline
model=Pipeline(
    steps=[
        ("preprocessor",preprocessor),
        ("classifier",LogisticRegression(max_iter=1000))
    ]
)

#split dataset
X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
# Train
print("Training Model....")
model.fit(X_train,y_train)
print("Training Completed !")

#Prediction
y_pred=model.predict(X_test)

#Accuracy

accuracy = accuracy_score(y_test,y_pred)
print(f"\n Accuracy :{accuracy:.4f}")
