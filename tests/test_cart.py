from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_add_item():
    response = client.post("/add/", json={"name": "Apple", "price": 1.5, "quantity": 2})
    assert response.status_code == 200
    assert response.json() == {"message": "Added 2 of Apple to the cart."}

def test_get_cart():
    response = client.get("/cart/")
    assert response.status_code == 200
    assert len(response.json()['cart']) > 0
