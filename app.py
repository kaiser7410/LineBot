from flask import Flask, request
import requests
import os
from dotenv import load_dotenv
import json
from bot_modules.lineModules import sendRelpyMseeage
from bot_modules.usdt_price_get import max_usdt, rybit_usdt, bito_usdt
from bot_modules.binanceApi import get_binance_prices, get_binance_one_price

app = Flask(__name__)

# 取得環境設定
load_dotenv()
LINE_TOKEN = os.getenv("LINE_TOKEN")


# 定義掛勾line bot 服務
@app.route("/api/v1/webhook/service", methods=["POST"])
def webhookProcess():
    response = None
    json_file = request.get_json()
    
    # 取通用屬性 user id replytoken
    data = json_file['events'][0]

    source = data['source']
    userid = None
    # 判斷是否為個人使用者
    if source['type'] == 'user':
        userid = source['userId']
        print(userid)
    # 判斷訊息是哪一種事件type(follow/message/unfollow...)
    if data['type'] == 'follow':
        replyToken = data['replyToken']
        print(f'userid:{userid} replytoken:{replyToken}')
        content = '歡迎使用幣圈小工具\n目前功能有:\n1. 查詢USDT/TWD價格 (輸入USDT 不分大小寫)\n2. 查詢主流幣，如BTC,ETH和SOL (輸入BTC or ETH or SOL 不分大小寫)'
        sendRelpyMseeage(LINE_TOKEN, replyToken, content)
        return ""
    if data['type'] == 'message':
        replyToken = data['replyToken']
        messageObj = data['message']
        # 判斷聊天室內容是文字
        if messageObj['type'] == 'text':
            # content = messageObj['text']
            # # 已讀已回鸚鵡
            # sendRelpyMseeage(LINE_TOKEN, replyToken, content)
            if messageObj['text'].lower() == 'usdt':
                max_price = max_usdt()
                bito_price = bito_usdt()
                rybit_price = rybit_usdt()
                content = f'Max: {max_price}TWD\nBito: {bito_price}TWD\nRybit: {rybit_price}TWD'
                sendRelpyMseeage(LINE_TOKEN, replyToken, content)
            elif messageObj['text'].lower() == 'btc':
                btc_price = get_binance_one_price('BTCUSDT')
                content = f'Binance\nBTC/USDT: {btc_price} USDT'
                sendRelpyMseeage(LINE_TOKEN, replyToken, content)
            elif messageObj['text'].lower() == 'eth':
                eth_price = get_binance_one_price('ETHUSDT')
                content = f'Binance\nETH/USDT: {eth_price} USDT'
                sendRelpyMseeage(LINE_TOKEN, replyToken, content)
            elif messageObj['text'].lower() == 'sol':
                sol_price = get_binance_one_price('SOLUSDT')
                content = f'Binance\nSOL/USDT: {sol_price} USDT'
                sendRelpyMseeage(LINE_TOKEN, replyToken, content)

    return ""

if __name__ == "__main__":
    app.run()