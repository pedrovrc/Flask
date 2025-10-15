from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_list_initially_empty(client):
    rv = client.get("/tasks")
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_create_task(client):
    rv = client.post("/tasks", json={"title": "Comprar leite"})
    assert rv.status_code == 201
    t = rv.get_json()
    assert t["id"] == 1
    assert t["title"] == "Comprar leite"
    assert t["done"] is False

def test_get_task(client):
    client.post("/tasks", json={"title": "Fazer exercício"})
    rv = client.get("/tasks/1")
    assert rv.status_code == 200
    t = rv.get_json()
    assert t["title"] == "Fazer exercício"

def test_update_task(client):
    client.post("/tasks", json={"title": "Ler livro"})
    rv = client.put("/tasks/1", json={"done": True})
    assert rv.status_code == 200
    t = rv.get_json()
    assert t["done"] is True

def test_delete_task(client):
    client.post("/tasks", json={"title": "Apagar depois"})
    rv = client.delete("/tasks/1")
    assert rv.status_code == 204

    rv = client.get("/tasks/1")
    assert rv.status_code == 404

def test_create_without_title_returns_400(client):
    rv = client.post("/tasks", json={})
    assert rv.status_code == 400

def test_get_nonexistent_returns_404(client):
    rv = client.get("/tasks/999")
    assert rv.status_code == 404