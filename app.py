import requests as r
import json

api = "https://api.qwer.pw/request/hangang_temp?apikey=guest"
with open("./config/hanriver/api.json", "wb") as file:
    response = r.get(api)
    file.write(response.content)

with open("./config/hanriver/api.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    temp = data[1]["respond"]["temp"]

print("현재 한강수온은 " + temp + "도 입니다.")