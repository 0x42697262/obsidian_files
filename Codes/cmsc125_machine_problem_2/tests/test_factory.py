from machine_problem_2 import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING' : True}).testing


def test_index(client):
    response    = client.get('/')
    assert response.data == b'index() page'
