from fastapi.testclient import TestClient
from fastdemo.main import app


client = TestClient(app)


def test_root():
    resp = client.get("/")

    expected = {"Hello": "World"}

    assert resp.status_code == 200
    assert resp.json() == expected


def test_read_items():
    resp = client.get("/items/1")

    expected = {"item_id": 1, "q": None}

    assert resp.status_code == 200
    assert resp.json() == expected


def test_read_items_query():
    resp = client.get("items/1?q=hello")

    expected = {"item_id": 1, "q": "hello"}

    assert resp.status_code == 200
    assert resp.json() == expected
