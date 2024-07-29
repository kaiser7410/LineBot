import requests
import json

# 常數架構
replyMessageURL = 'https://api.line.me/v2/bot/message/reply'

# 回復訊息到使用者端(借助ReplyToken)
def sendRelpyMseeage(token, replytoken, message):
    ltoken = "Bearer " + token
    # 建構Header(dict物件)
    myHeaders = {"Authorization": ltoken, "Content-Type": "application/json"}
    message = [{"type": "text", "text": message}]
    try:
        # 回送資料
        data = {"replyToken": replytoken, "messages": message}
        requests.post(replyMessageURL, data=json.dumps(data), headers=myHeaders)
    except Exception as ex:
        raise ex
