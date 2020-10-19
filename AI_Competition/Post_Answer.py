import json
import requests
import Get
import AI_Test
url ="http://47.102.118.1:8089/api/challenge/submit"
data = {
    "uuid": Get.uuid,
    "teamid": 13,
    "token": "2e572ce3-cfd0-4d41-b966-b3efc244f45f",
    "answer": {
        "operations": AI_Test.zero_way,
        "swap": AI_Test.answer_swap
    }
}
r = requests.post(url,json=data)
print(AI_Test.zero_way)
print(AI_Test.answer_swap)
print(r.text)