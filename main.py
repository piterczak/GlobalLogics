from typing import Union
from fastapi import FastAPI


sklep = FastAPI()

@sklep.get("/")
def read_front_page():
    return {"Hello": "World"}

@sklep.get("/products/product/{item_id}")
def read_products(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

