"""
Swap Numbers API ke tests - CI mein yeh automatically chalenge.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    """Root endpoint check."""
    r = client.get("/")
    assert r.status_code == 200
    assert "Swap Numbers" in r.json()["message"]


def test_swap_numbers():
    """Swap sahi kaam karta hai."""
    r = client.post("/swap?a=5&b=10")
    assert r.status_code == 200
    data = r.json()
    assert data["a"] == 10
    assert data["b"] == 5
    assert data["message"] == "Swapped successfully"


def test_swap_negative():
    """Negative numbers bhi swap honi chahiye."""
    r = client.post("/swap?a=-3&b=7")
    assert r.status_code == 200
    assert r.json()["a"] == 7
    assert r.json()["b"] == -3
