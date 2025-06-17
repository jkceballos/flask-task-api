import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json == {"message": "Flask Task API"}

def test_add_and_get_task(client):
    resp = client.post('/tasks', json={"title": "Test"})
    assert resp.status_code == 201
    assert resp.json["title"] == "Test"

    resp2 = client.get('/tasks')
    assert len(resp2.json) >= 1

def test_delete_task(client):
    client.post('/tasks', json={"title": "ToDelete"})
    resp = client.delete('/tasks/1')
    assert resp.status_code == 204
