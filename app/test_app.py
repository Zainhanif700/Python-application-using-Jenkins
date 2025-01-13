import pytest
from . import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_hello(client):
    response = client.get('/')
    assert response.data == b'Hello, Jenkins CI/CD with Flask!'
    assert response.status_code == 200
