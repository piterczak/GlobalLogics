#A python application with mix of FastAPI 
#that works as a shop on a Uvicorn werb server and JSON file.

from typing import Union, List
from fastapi import FastAPI
from models import Product
import click
import json

#Application named Shop created with FastAPI
shop = FastAPI()

#DataBase with list of products that will be in store.
database: List[Product] = [
    Product(
        #id = uuid4(),
        name = "Apples",
        warehouse_count = 50,
        ),
    Product(
        #id = uuid4(),
        name = "Bananas",
        warehouse_count = 50,
    ), 
    Product(
        #id = uuid4(),
        name = "Oranges",
        warehouse_count = 50,
    ), 
    Product(
        #id = uuid4(),
        name = "Strawberries",
        warehouse_count = 50,
    ), 
]


@shop.get("/")  #Navigate to main page
async def root():
    return{"Welcome to the shop": "!"}


"""print("Please provide what you'd like to do")
#while True:
print("Choose 1 to show current status of warehouse items")
print("Choose 2 to buy products")
print("Choose 3 to exit shop")
option = input()
if option == "1":"""
@shop.get("/products_list")  #Navigate to main page
async def product_list():
    counter = 0
    temp_dict = {"Name": [], "Warehouse_count": []}
    while counter < len(database):
        temp_dict["Name"].append(database[counter].name)
        temp_dict["Warehouse_count"].append(database[counter].warehouse_count)
        counter += 1
    """temp_json = json.dumps(database)
    with open(temp_json) as json_file:
        data = json.load(json_file)
        print(data)"""
    return {"List of products ":temp_dict}
"""if option == "2":"""

@shop.get("/products_list/{product_name}/buy_count/{buy_count}")
async def buy_product(product_name: str, buy_count: int):
    product_name = product_name
    buy_count = buy_count
    temp_dict = {"Name": [], "Warehouse_count": []}
    counter = 0
    while counter < len(database):
        temp_dict["Name"].append(database[counter].name)
        temp_dict["Warehouse_count"].append(database[counter].warehouse_count)
        counter += 1
    counter = 0
    while counter < len(database):
        if temp_dict["Name"][counter] == product_name:
            if temp_dict["Warehouse_count"][counter] >= buy_count:
                temp_dict["Warehouse_count"][counter] = temp_dict["Warehouse_count"][counter] - buy_count
            else:
                return {"Can't buy following item because there's not enough in stock": temp_dict["Name"][counter] + " In stock: "+  str(temp_dict["Warehouse_count"][counter])}

        counter += 1
    return {"List of products ": temp_dict}


"""   if option == "3":
    break"""

#@shop.post("/buy/{product_name}/")

