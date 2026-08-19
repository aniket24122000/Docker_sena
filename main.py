import os
from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is missing")

@app.get("/")
def home():
    return {
        "message": "Application is running",
        "database": DATABASE_URL
    }