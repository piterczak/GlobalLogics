# A python application with mix of FastAPI
# that works as a shop on a Uvicorn werb server and JSON file.
from fastapi import FastAPI
import json

shop = FastAPI()  # Application named Shop created with FastAPI

# DataBase with list of products that will be in store in JSON file.
filename = "./data/warehouse.json"
database = filename


# Main page of the web server
@shop.get("/")
async def root():
    return{"Welcome to the shop": "!"}


# Page that returns items from database as JSON
@shop.get("/products_list")
async def product_list():
    with open(filename, "r") as f:
        temp = json.load(f)
    return {"List of products ": temp}


# Page that allows user to buy item, substracting value from JSON database
@shop.get("/products_list/{product_name}/buy_count/{buy_count}")
async def buy_product(product_name: str, buy_count: int):
    with open(filename, "r") as f:
        temp = json.load(f)
        f.close()
        index = 0
        flag = True
        while index < len(temp):
            for key, val in temp[index].items():
                if key == product_name:
                    if buy_count == 0:
                        return {"Can't buy 0 items!"}
                    elif val >= buy_count:
                        val = val - buy_count
                        temp[index] = {key: val}
                        flag = False
                        break
                    elif val < buy_count:
                        return {"Not enough items in warehouse! ": key +
                                "in stock: " +
                                str(val)}
                else:
                    return {"There's no item like that in warehouse!"}
            if not flag:
                break
            index += 1

    with open(filename, "w") as f:
        json.dump(temp, f, indent=1)
    with open(filename, "r") as f:
        temp = json.load(f)
    return {"List of products ": temp}


