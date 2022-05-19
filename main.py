from typing import Union
from fastapi import FastAPI


shop = FastAPI()

@shop.get("/")
def root():
    return {"Hello": "World"}

@shop.get("/products/product/{item_id}")
def read_products(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

