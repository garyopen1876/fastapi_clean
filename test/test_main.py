from app.main import app
from dotenv import load_dotenv
from fastapi.testclient import TestClient

client = TestClient(app)
load_dotenv()  # you need to load env !!


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


# def test_login():
#     # Successful
#     body = {"username": "string", "password": "string"}
#     headers = {"content-type": "application/x-www-form-urlencoded"}
#     response = client.post("/login", json=body, headers=headers)
#     assert response.status_code == 200
#     # User or Password error
#     body = {"username": "", "password": ""}
#     response = client.post("/login", json=body)
#     assert response.status_code == 401
#     # Data lack
#     body = {"password": ""}
#     response = client.post("/login", json=body)
#     assert response.status_code == 422
#     body = {"username": ""}
#     response = client.post("/login", json=body)
#     assert response.status_code == 422
#     response = client.post("/login")
#     assert response.status_code == 422


# def test_user():
#     body = {"username": "string", "password": "string"}
#     response = client.post("/login", json=body)
#     token = response.json()["token"]
#     body = {"username": "test", "password": "test", "email": "test@mail.com"}
#     response = client.post("/user", headers={"token": token}, json=body)
#     assert response.status_code == 201
#     # User existed
#     body = {"username": "test", "password": "test", "email": "test@mail.com"}
#     response = client.post("/user", headers={"token": token}, json=body)
#     assert response.status_code == 403
#     # Failed to authenticate token
#     token = "ABC"
#     body = {"username": "test", "password": "test", "email": "test@mail.com"}
#     response = client.post("/user", headers={"token": token}, json=body)
#     assert response.status_code == 402
#     # No token error
#     body = {"username": "test", "password": "test", "email": "test@mail.com"}
#     response = client.post("/user", json=body)
#     assert response.status_code == 403
