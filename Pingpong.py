# Nitro
# nitro0@naver.com
# 2/20/2020
import json
import requests

url = 'Service URL'
headers = {'Authorization': 'API Key',
            'Content-Type': 'application/json'}

def chat(text):
    data = dict()
    request = dict()
    request["query"] = text
    data["request"] = request # {"request":{"query":"text"}}
    return requests.post(url, headers=headers, data=json.dumps(data).encode('utf-8')) # Support utf-8 encode.

print(chat("안녕").text)