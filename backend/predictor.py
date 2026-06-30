import joblib

model = joblib.load("models/best_model.pkl")

def predict(data):
    prediction = model.predict(data)
    probability = model.predict_proba(data)

    return prediction, probability