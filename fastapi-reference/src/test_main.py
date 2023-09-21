from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/get")
    assert response.status_code == 200
    assert response.json() == {"user_agent":"testclient", "any_header": None}
