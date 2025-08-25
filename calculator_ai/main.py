from fastapi import FastAPI, Query
from .logic import add, subtract

app = FastAPI(title="Calculator AI", version="0.1.0")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/add")
def add_endpoint(a: float = Query(...), b: float = Query(...)):
    return {"result": add(a, b)}


@app.get("/subtract")
def subtract_endpoint(a: float = Query(...), b: float = Query(...)):
    return {"result": subtract(a, b)}
