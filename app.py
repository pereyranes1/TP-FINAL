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
import pandas as pd

X = pd.DataFrame([{
    "amount": data.amount,
    "oldbalanceOrg": data.oldbalanceOrg,
    "newbalanceOrig": data.newbalanceOrig,
    "oldbalanceDest": data.oldbalanceDest,
    "newbalanceDest": data.newbalanceDest,
    "step": data.step,
    "type_bin": data.type_bin
}])

X_scaled = scaler.transform(X)


    return {"fraude": int(pred)}
