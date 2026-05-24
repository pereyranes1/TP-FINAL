from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

modelo = joblib.load("modelo.pkl")
scaler = joblib.load("scaler.pkl")

class Transaccion(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
    step: int
    type_bin: int

@app.post("/predict")
def predict(data: Transaccion):
    X = np.array([[ 
        data.amount,
        data.oldbalanceOrg,
        data.newbalanceOrig,
        data.oldbalanceDest,
        data.newbalanceDest,
        data.step,
        data.type_bin
    ]])

    X_scaled = scaler.transform(X)
    pred = modelo.predict(X_scaled)[0]

    return {"fraude": int(pred)}
