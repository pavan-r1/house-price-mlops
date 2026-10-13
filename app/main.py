from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI(
    title="House Price Prediction API",
    description="MLOps Serving Endpoint for Real Estate Valuation",
    version="1.0.0"
)

class HouseFeatures(BaseModel):
    sqft: float
    bedrooms: int
    bathrooms: int
    neighborhood: str

@app.get("/")
def home():
    return {"status": "Online", "message": "Welcome to the House Price MLOps Prediction Service"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    return {"status": "success", "predicted_price_usd": 350000.0}
