import requests
import json
from bs4 import BeautifulSoup





user = input("아이디를 입력하세요\n")

url = 'https://api-aion.plaync.com/search/v1/characters?&query={}&serverId=21&site=aion&sort=rank&world=classic'.format(user)
req = requests.get(url).content

data = json.loads(req)

uid = data.get("documents")[0].get("charId")


srcurl = 'https://api-aion.plaync.com/game/v2/classic/merge/server/21/id/{}'.format(uid)
payload = {'keyList' : ["character_stats","character_equipments","character_abyss","character_stigma"]}
aionurl = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)

keySrc = json.dumps(payload,ensure_ascii=False)
reqsrc = requests.put(srcurl, json=payload).content

data2 = json.loads(reqsrc)
print(data2)
