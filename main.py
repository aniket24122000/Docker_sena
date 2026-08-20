from fastapi import FastAPI

app = FastAPI()

data = []

@app.get("/")
def home():
    return {"message": "FastAPI running"}

@app.get("/memory")
def consume_memory():
    # Intentionally allocate large memory
    data.append("A" * (100 * 1024 * 1024))

    return {
        "message": "Memory allocated",
        "chunks": len(data)
    }