import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

from src.utils.data_loader import load_data
from src.training.pipeline import create_preprocessor


# Load data
X, y = load_data()

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Preprocessor
preprocessor = create_preprocessor()

# Pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Hyperparameter grid
param_grid = {
    "classifier__n_estimators": [100, 200, 300],
    "classifier__max_depth": [5,10,20,None],
    "classifier__min_samples_split": [2, 5, 10],

}

# Grid Search
grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1,

)

# Trai"Searching best models")
grid.fit(X_train, y_train)



# Results
print("Best Parameters:")
print(grid.best_params_)

print("Best Score:")
print(grid.best_score_)
