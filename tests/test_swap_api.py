"""
AI-generated tests - yeh file har push par AI se automatically regenerate hoti hai.
Manual edits mat karo.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_app_loaded():
    """Placeholder - AI overwrite karega push par."""
    assert client.app is not None
