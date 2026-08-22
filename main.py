import os

from fastapi import FastAPI

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "unknown")

@app.get("/")
def home():
    return {
        "message": "FastAPI is running",
        "environment": APP_ENV
    }

@app.get("/health")
def health():
    return {
        "status": "UP",
        "environment": APP_ENV
    }