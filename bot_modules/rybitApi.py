import requests
import json

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

