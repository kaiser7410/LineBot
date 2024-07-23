import requests
import json


def get_binance_price(coin):
    url = 'https://api3.binance.com'
    api_url = f'{url}/api/v3/ticker/price?symbols={coin}'
    response = requests.get(api_url)
    get_json = response.json()
    price = {}
    for i in get_json:
        price[i["symbol"]] = i["price"]
    return price

