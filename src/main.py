import uvicorn
from fastapi import FastAPI, Depends
import joblib
import pandas as pd
from pydantic import BaseModel
from typing import List

app = FastAPI()
model = joblib.load("../model/attrition_classification_model.pkl")

class InputData(BaseModel):
    Age:int
    Years_at_Company:int
    Average_Monthly_Hours:int
    Salary:int
    Satisfaction_Level:float
    Gender:str
    Department:str
    Promotion_Last_5Years:int

@app.post("/predict/")
def predict(data: List[InputData]):
    #df = pd.DataFrame(data)
    df = pd.DataFrame([item.dict() for item in data])
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}


# @app.post("/predict/")
# def predict(data: list[InputData]):  # Expecting a **list** of InputData
#     return {"message": "Data received", "data": data}

