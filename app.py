from flask import Flask, request
import requests
import os
from dotenv import load_dotenv
import json
from bot_modules.lineModules import sendRelpyMseeage

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
    if data['type'] == 'message':
        replyToken = data['replyToken']
        messageObj = data['message']
        # 判斷聊天室內容是文字
        if messageObj['type'] == 'text':
            content = messageObj['text']
            # 已讀已回鸚鵡
            sendRelpyMseeage(LINE_TOKEN, replyToken, content)
            pass
    return ""

if __name__ == "__main__":
    app.run()