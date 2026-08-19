from fastapi import FastAPI
from pathlib import Path

app = FastAPI()

DATA_DIR = Path("/app/data")
DATA_DIR.mkdir(exist_ok=True)

@app.post("/save")
def save_data():
    file = DATA_DIR / "users.txt"

    with open(file, "a") as f:
        f.write("Aniket\n")

    return {"message": "Data saved"}


@app.get("/users")
def get_users():
    file = DATA_DIR / "users.txt"

    if not file.exists():
        return {"users": []}

    with open(file, "r") as f:
        users = f.read().splitlines()

    return {"users": users}