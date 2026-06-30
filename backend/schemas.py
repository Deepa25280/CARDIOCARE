from pydantic import BaseModel

class PatientData(BaseModel):
    age: int
    sex: str
    cp: str
    trestbps: float
    chol: float
    fbs: bool
    restecg: str
    thalch: float
    exang: bool
    oldpeak: float
    slope: str
    ca: float
    thal: str