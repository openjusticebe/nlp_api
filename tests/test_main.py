from starlette.testclient import TestClient


def test_root_endpoint(testclient: TestClient):
    r = testclient.get("/")
    assert r.status_code == 200


def tokenisation(testclient: TestClient):
    data = {"text": "Les membres d'OpenJustice aiment les Pizzas Margherita"}
    r = testclient.post("/tools/tokenisation", json=data)
    assert r.status_code == 200, r.text
    assert r.json()["text"] == data["text"]


def sentiment_analysis(testclient: TestClient):
    data = {"text": "Les membres d'OpenJustice aiment les Pizzas Margherita"}
    r = testclient.post("/tools/sentiment_analysis", json=data)
    assert r.status_code == 200, r.text
    assert r.json()["text"] == data["text"]