import requests
import json


# Max交易所
def max_usdt():
    # 例外管理
    # 查詢價格的幣種
    coin = 'usdttwd'
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
    
# Rybit交易所
def rybit_usdt():
    try:
        url = 'https://www.rybit.com/wallet-api/v1/kgi/exchange-rates/?symbol=USDT_TWD&client_id=rybit_web_v2024.06.06.90&device_id=97525753-628e-403a-8de3-6dd95004be53&fp_did=unknown&app_ver=v2024.06.06.90&tz_name=Asia%2FTaipei&tz_offset=28800&sys_lang=zh-TW&app_lang=zh-TW'

        # 取得價格json檔
        result = requests.get(url).text
        # print(result)

        # 使用json.loads 將 result text檔 轉換成 json檔
        price = json.loads(result)["data"]
        # 取得USDT/TWD購買價格
        buy_price = price["buy_rate"]
        # 取得USDT/TWD販賣價格
        sell_price= price["sell_rate"]
        # print(f"Sending price_update_Rybit: {buy_price}")  # 調試信息
        return buy_price
        
    except Exception as ex:
        print(f"Error: {ex}")

# Bito交易所
def bito_usdt():
    # 查詢價格的幣種
    coin = 'usdt_twd'
    # 例外管理
    try:
        # bito網站url
        url = "https://api.bitopro.com"
        # 定義取得幣種價格的網址
        urlstring = f'{url}/v3/tickers/{coin}'
        # 使用前端Http Client採用GET方式提出請求
        response = requests.get(urlstring)
        get_json = response.json()  # dict物件
        usdt_price = get_json['data']['lastPrice']
        return usdt_price
    except Exception as ex:
        raise Exception('錯誤') #拋出例外物件 重新建構配置訊息


