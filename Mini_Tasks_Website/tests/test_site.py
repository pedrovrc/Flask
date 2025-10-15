import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_initially_empty(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Nenhuma tarefa ainda" in rv.data or b"Nenhuma tarefa" in rv.data

def test_create_task_and_list(client):
    rv = client.post("/create", data={"title": "Comprar leite", "content": "2 litros"}, follow_redirects=True)
    assert rv.status_code == 200
    assert b"Tarefa criada" in rv.data or b"Tarefa criada com sucesso" in rv.data
    # agora deve conter o título na página
    rv = client.get("/")
    assert b"Comprar leite" in rv.data

def test_edit_task(client):
    client.post("/create", data={"title": "Old", "content": "X"})
    # abrir a página de edição
    rv = client.get("/edit/1")
    assert rv.status_code == 200
    # enviar atualização
    rv = client.post("/edit/1", data={"title": "New", "content": "Y"}, follow_redirects=True)
    assert b"Tarefa atualizada" in rv.data or b"Tarefa atualizada com sucesso" in rv.data
    # verificar mudança
    rv = client.get("/")
    assert b"New" in rv.data
    assert b"Old" not in rv.data

def test_delete_task(client):
    client.post("/create", data={"title": "ToDelete", "content": ""})
    rv = client.post("/delete/1", follow_redirects=True)
    assert b"Tarefa removida" in rv.data or b"Tarefa removida" in rv.data
    rv = client.get("/")
    assert b"ToDelete" not in rv.data

def test_edit_nonexistent(client):
    rv = client.post("/edit/999", data={"title":"x","content":"y"}, follow_redirects=True)
    # behavior: redirect to index with flash error
    assert rv.status_code == 200
    assert b"Tarefa nao encontrada" in rv.data or b"nao encontrada" in rv.data

def test_delete_nonexistent(client):
    rv = client.post("/delete/999", follow_redirects=True)
    assert rv.status_code == 200
    assert b"Tarefa nao encontrada" in rv.data or b"nao encontrada" in rv.data

def test_create_task_without_title(client):
    rv = client.post("/create", data={"title": "", "content": "No title"}, follow_redirects=True)
    assert rv.status_code == 200
    assert b"O titulo e obrigatorio" in rv.data or b"O titulo e obrigatorio" in rv.data
    # ainda não deve ter tarefas
    rv = client.get("/")
    assert b"Nenhuma tarefa ainda" in rv.data or b"Nenhuma tarefa" in rv.data