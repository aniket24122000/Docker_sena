import os
import mysql.connector
from fastapi import FastAPI

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "localhost")

@app.get("/")
def home():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user="root",
        password="root",
        database="testdb"
    )

    connection.close()

    return {"message": "Database connection successful"}