import os
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from src.utils.data_loader import load_data
from src.training.pipeline import create_preprocessor


def train_best_model():

    # Load data
    X, y = load_data()

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
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

    # Hyperparameter Grid
    param_grid = {
        "classifier__n_estimators": [100, 200, 300],
        "classifier__max_depth": [None, 10, 20],
        "classifier__min_samples_split": [2, 5],
        "classifier__min_samples_leaf": [1, 2],
        "classifier__max_features": ["sqrt", "log2"]
    }

    # Grid Search
    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv=5,
        scoring="accuracy",
        n_jobs=-1,
        verbose=2
    )

    print("Training Random Forest...")
    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    # Predictions
    y_pred = best_model.predict(X_test)

    print("\n==============================")
    print("BEST PARAMETERS")
    print("==============================")
    print(grid_search.best_params_)

    print("\nCross Validation Accuracy:")
    print(f"{grid_search.best_score_:.4f}")

    print("\nTest Accuracy:")
    print(f"{accuracy_score(y_test, y_pred):.4f}")

    print("\nPrecision:")
    print(f"{precision_score(y_test, y_pred):.4f}")

    print("\nRecall:")
    print(f"{recall_score(y_test, y_pred):.4f}")

    print("\nF1 Score:")
    print(f"{f1_score(y_test, y_pred):.4f}")

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    # Save Model
    os.makedirs("models", exist_ok=True)

    joblib.dump(best_model, "models/best_model.pkl")
    print("\n"+"="*60)

    print("\nBest model saved to:")
    print("models/best_model.pkl")
    print("="*60)


if __name__ == "__main__":
    train_best_model()