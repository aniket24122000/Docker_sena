import os
from fastapi import FastAPI

DATABASE_URL = os.environ["DATABASE_URL"]

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI is running"
    }