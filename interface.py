import requests
import json
import time


shop_url = "http://127.0.0.1:8000/products_list"

def view_shop(shop_url):
    response = requests.get(shop_url)
    json_response = json.loads(response.text)
    print(json_response)

def buy_item(product_name, buy_count):
    buy_item_url = "http://127.0.0.1:8000/products_list/"+ product_name+ "/buy_count/"+ buy_count
    response = requests.get(buy_item_url)
    json_response = json.loads(response.text)
    if response.status_code == 200:
        print("Successfully bought "+ buy_count + " " + product_name )
    print(json_response)



while True:
    print("Please specify what would you like to do by choosing relevant option")
    print("Type 1 to view number of products in shop")
    print("Type 2 to buy item from shop")
    print("Type 3 to exit application")
    choose = input()
    if choose == "1":
        view_shop(shop_url)
        print("")
    if choose == "2":
        print("Please provide what item you want to buy")
        product_name = input(str)
        print("Please specify the number of " + product_name + " you'd like to buy")
        buy_count = input(int)
        buy_item(product_name, buy_count)
    if choose == "3":
        print("Goodbye!")
        time.sleep(3)
        break





