#A python application with mix of FastAPI 
#that works as a shop on a Uvicorn werb server and JSON file.

from fastapi import FastAPI
import json

#Application named Shop created with FastAPI
shop = FastAPI()

#DataBase with list of products that will be in store in JSON file.
filename = "./data/warehouse.json"
database = filename

@shop.get("/")  #to main page
async def root():
    return{"Welcome to the shop": "!"}

@shop.get("/products_list")  #page that returns items from database as JSON
async def product_list():
    with open (filename, "r") as f:
        temp = json.load(f)
    return {"List of products ":temp}

@shop.get("/products_list/{product_name}/buy_count/{buy_count}") #page that allows user to buy item, substracting value from JSON database
async def buy_product(product_name: str, buy_count: int):
    with open(filename, "r") as f:
        temp = json.load(f)
        f.close()
        index = 0
        while index < len(temp):
            for key, val in temp[index].items():
                if key == product_name:
                    if val >= buy_count:
                        val = val - buy_count
                        temp[index] = {key: val}
                    else:
                        return {"Not enough items in warehouse! ": key + "in stock: " + str(val)}
            index += 1
    with open(filename, "w") as f:
        json.dump(temp, f, indent = 1)
    with open(filename, "r") as f:
        temp = json.load(f)
    return {"List of products ": temp}


