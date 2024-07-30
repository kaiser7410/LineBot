import requests
import json



'''
幣種代號(範例): 'BTCUSDT', 'ETHUSDT', 'SOLUSDT'....
'''

# 一次取得多個幣種
def get_binance_prices(coin):
    url = 'https://api3.binance.com'
    api_url = f'{url}/api/v3/ticker/price?symbols={coin}'
    response = requests.get(api_url)
    get_json = response.json()
    price = {}
    for i in get_json:
        price[i["symbol"]] = i["price"]
    return price

# 一次取得一種幣種
def get_binance_one_price(coin):
    url = 'https://api3.binance.com'
    api_url = f'{url}/api/v3/ticker/price?symbol={coin}'
    response = requests.get(api_url)
    get_json = response.json()
    price = get_json['price']
    return price
