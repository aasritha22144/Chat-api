from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_message():
    response = client.post("/messages", json={
        "user": "Alice",
        "message": "Hello"
    })
    assert response.status_code == 201

def test_get_all_messages():
    response = client.get("/messages")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_messages_by_user():
    response = client.get("/messages/Alice")
    assert response.status_code == 200

def test_missing_user_or_message():
    response = client.post("/messages", json={"user": ""})
    assert response.status_code == 400

def test_nonexistent_user():
    response = client.get("/messages/UnknownUser")
    assert response.status_code == 200
    assert response.json() == []

def test_clear_messages():
    response = client.delete("/messages")
    assert response.status_code == 200
    assert response.json()["status"] == "cleared"
