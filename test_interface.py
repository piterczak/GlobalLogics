from fastapi.testclient import TestClient
from main import shop
import interface

client = TestClient(shop)

def test_view_shop():
    response = client.get("/products_list")
    assert response.status_code == 200
    assert type(response.json()['List of products ']) == list

def test_buy_item_pass():
    response = interface.buy_item("Apples", 5)
    assert response 