import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)
from sklearn.metrics import accuracy_score
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

# Create preprocessing pipeline
preprocessor = create_preprocessor()

# Build pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Hyperparameter grid
param_grid = {
    "classifier__n_estimators": [100, 200,300],
    "classifier__max_depth": [10, 20,None],
    "classifier__min_samples_split": [2, 5],
    "classifier__min_samples_leaf": [1, 2],
    
}

# Grid Search
grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1,
)

print("Searching for best parameters...")

grid_search.fit(X_train, y_train)

print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest Cross Validation F1 Score:")
print(grid_search.best_score_)

# Evaluate on test data
best_model = grid_search.best_estimator_

predictions = best_model.predict(X_test)

print("\nTest Accuracy:")
print(accuracy_score(y_test, predictions))