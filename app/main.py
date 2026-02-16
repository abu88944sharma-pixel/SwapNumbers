"""
Swap Numbers API - Two numbers swap karta hai.
"""
from fastapi import FastAPI

app = FastAPI(title="Swap Numbers API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Swap Numbers of the APIqwerty - use POST /swap"}


@app.post("/swap")
def swap_numbers(a: int, b: int):
    """Do numbers lo, swap karke return karo."""
    return {"a": b, "b": a, "message": "Swapped successfully"}
