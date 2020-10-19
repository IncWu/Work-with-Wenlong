import json
import requests
url ="http://47.102.118.1:8089//api/challenge/create"
data = {
    "teamid": 13,
    "data": {
        "letter": "c",
        "exclude": 7,
        "challenge": [
            [8, 5, 9],
            [4, 0, 1],
            [6, 3, 2]
        ],
        "step": 10,
        "swap": [2,5]
    },
    "token": "2e572ce3-cfd0-4d41-b966-b3efc244f45f"
}
r = requests.post(url,json=data)
print(r.text)