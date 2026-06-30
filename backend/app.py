import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from backend.schemas import PatientData
from backend.predictor import predict

app = FastAPI(
    title="CardioCare AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CardioCare AI"
    }
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict_heart_disease(patient: PatientData):

    df = pd.DataFrame([patient.model_dump()])

    prediction, probability = predict(df)

    return {
        "prediction": int(prediction[0]),
        "probability": float(max(probability[0]))
    }