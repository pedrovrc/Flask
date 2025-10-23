"""
test_app.py: Pytest tests for Database_and_API project.
"""
import pytest
from app import create_app
from models import db, Task

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_task(client):
    response = client.post('/api/v1/tasks/', json={'title': 'Nova tarefa'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Nova tarefa'
    assert not data['done']

def test_list_tasks(client):
    client.post('/api/v1/tasks/', json={'title': 'Tarefa 1'})
    client.post('/api/v1/tasks/', json={'title': 'Tarefa 2'})
    response = client.get('/api/v1/tasks/')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2

def test_update_task(client):
    response = client.post('/api/v1/tasks/', json={'title': 'Editar'})
    task_id = response.get_json()['id']
    response = client.put(f'/api/v1/tasks/{task_id}', json={'title': 'Editada', 'done': True})
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Editada'
    assert data['done']

def test_delete_task(client):
    response = client.post('/api/v1/tasks/', json={'title': 'Deletar'})
    task_id = response.get_json()['id']
    response = client.delete(f'/api/v1/tasks/{task_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 'ok'

def test_invalid_title(client):
    response = client.post('/api/v1/tasks/', json={'title': ''})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_not_found(client):
    response = client.get('/api/v1/tasks/999')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data