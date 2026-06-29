import pandas as pd

from src.training.models import models
from src.training.pipeline import create_preprocessor
from src.utils.data_loader import load_data

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def main():

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

    # Create preprocessor
    preprocessor = create_preprocessor()

    results = []

    # Train and evaluate each model
    for name, classifier in models.items():

        model = Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", classifier)
        ])

        # Train
        model.fit(X_train, y_train)

        # Predict
        predictions = model.predict(X_test)

        # Store metrics
        results.append({
            "Model": name,
            "Accuracy": accuracy_score(y_test, predictions),
            "Precision": precision_score(y_test, predictions),
            "Recall": recall_score(y_test, predictions),
            "F1 Score": f1_score(y_test, predictions)
        })

    # Convert to DataFrame
    results_df = pd.DataFrame(results)

    # Sort by Accuracy
    results_df = results_df.sort_values(
        by="Accuracy",
        ascending=False
    )

    print(results_df)


if __name__ == "__main__":
    main()