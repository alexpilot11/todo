from fastapi.testclient import TestClient
from todo.main import app
from todo.fake_db.items import items


client = TestClient(app)


def test_root():
    resp = client.get("/")
    expected = {"Hello": "World"}
    assert resp.status_code == 200, resp.json()
    assert resp.json() == expected


def test_read_items():
    resp = client.get("/items")
    assert resp.status_code == 200, resp.json()
    assert resp.json() == items


def test_read_items_query():
    resp = client.get("items?q=f")
    expected = items[:1]
    assert resp.status_code == 200, resp.json()
    assert resp.json() == expected


def test_read_item_detail():
    resp = client.get("/items/2")
    # print(resp).json()
    assert resp.status_code == 200, resp.json()
    assert resp.json() == items[1]
