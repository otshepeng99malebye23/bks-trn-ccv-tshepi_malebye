#import pytest
#import httpx
from api_integration import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_validate_true():
    response = client.get("/validate/2222405343248877")
    assert response.status_code == 200
    assert response.json() == {"number": "2222405343248877", "valid": True}

def test_validate_false():
    response = client.get("/validate/2222405343248878")
    assert response.status_code == 200
    assert response.json() == {"number": "2222405343248878", "valid": False}
