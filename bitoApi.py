import requests

# Restful API 
# 查詢價格的幣種
coin = 'usdt_twd'

def bito_usdt(market):
    # 例外管理
    try:
        # bito網站url
        url = "https://api.bitopro.com"
        # 定義取得幣種價格的網址
        urlstring = f'{url}/v3/tickers/{market}'
        # 使用前端Http Client採用GET方式提出請求
        response = requests.get(urlstring)
        get_json = response.json()  # dict物件
        usdt_price = get_json['data']['lastPrice']
        return usdt_price
    except Exception as ex:
        raise Exception('錯誤') #拋出例外物件 重新建構配置訊息
