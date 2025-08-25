from fastapi.testclient import TestClient
from calculator_ai.main import app

client = TestClient(app)


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_add_api():
    r = client.get("/add", params={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5.0


def test_subtract_api():
    r = client.get("/subtract", params={"a": 10, "b": 7.5})
    assert r.status_code == 200
    assert r.json()["result"] == 2.5
