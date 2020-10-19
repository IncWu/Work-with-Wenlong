import json
import requests
import re
import base64

url ="http://47.102.118.1:8089/api/challenge/start/ae39a052-3a75-40cb-858c-bd6de923ff83"
data = {
    "teamid": 13,
    "token": "2e572ce3-cfd0-4d41-b966-b3efc244f45f"
}
r = requests.post(url,json=data)
r.raise_for_status()
r.encoding = r.apparent_encoding
dic=json.loads(r.text)
img = base64.b64decode(dic["data"]["img"])
step=dic["data"]["step"]
swap=dic["data"]["swap"]
uuid=dic['uuid']
print(dic)
print(step)
print(swap)
print(uuid)
with open("D:/Python/software_engineering/GAME/Question/Full_Image.png", "wb") as fp:
    fp.write(img)  # 900*900