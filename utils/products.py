# utils/products.py

import requests

from config.settings import BASE_URL

def get_product_id(symbol):

    url = f"{BASE_URL}/v2/products"

    products = requests.get(url).json()["result"]

    for product in products:

        if product["symbol"] == symbol:

            return product["id"]

    return None