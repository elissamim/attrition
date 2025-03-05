from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("../model/attrition_classification_model.pkl")

@app.post("/predict/")
def predict(data: list):
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}
