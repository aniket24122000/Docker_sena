import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    response = requests.get("https://httpbin.org/get")

    return {
        "message": "API is working",
        "status": response.status_code
    }