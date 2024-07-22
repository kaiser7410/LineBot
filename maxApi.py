import requests



# 查詢價格的幣種
coin = 'usdttwd'

def max_usdt(coin):
    # 例外管理
    try:
        # max網站url
        url = "https://max-api.maicoin.com"
        # 定義取得幣種價格的網址
        urlstring = f'{url}/api/v2/tickers/{coin}'
        # 使用前端Http Client採用GET方式提出請求
        response = requests.get(urlstring)
        get_json = response.json()
        usdt_price = get_json["last"]
        return usdt_price
    except Exception as ex:
        raise Exception('錯誤') #拋出例外物件 重新建構配置訊息
    

