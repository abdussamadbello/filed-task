from fastapi.testclient import TestClient
from app import app
from test_data import correct_songdata, incorrect_songdata,poddata

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
    
def test_get_item():
    response = client.get("/song/ ")
    assert response.status_code == 200
    response = client.get("/items/12345")
    assert response.status_code == 400
    response = client.get("/items/ ")
    assert response.status_code == 400
    assert response.json() == {"detail": "path doesn't exists"}

def test_create_item():
    response = client.post("/song",json=correct_songdata)
    assert response.status_code == 200
    response = client.post("/song", json=incorrect_songdata)
    assert response.status_code == 400
    response = client.post("/items",json=correct_songdata)
    assert response.status_code == 400
    
def test_update_item():
    response = client.put("/song/604e2cc3b897154f7d8e9bd9",json=correct_songdata)
    assert response.status_code == 200
    response = client.put("/song/604e2cc3b897154f7d8e9bd9", json=incorrect_songdata)
    assert response.status_code == 400
    response = client.put("/items/ ",json=correct_songdata)
    assert response.status_code == 400

def test_delete_item():
    response = client.delete("/song/123")
    assert response.status_code == 400
    response = client.delete("/song/cc3b897154f7d8e9bd9")
    assert response.status_code == 400
    response = client.delete("/items/ ")
    assert response.status_code == 400
