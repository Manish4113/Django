import json

import requests

URL='http://127.0.0.1:8000/stucreate'

data={
    'name':'Manish',
    'roll':101,
    'city':'Jalaun'
}

json_data=json.dumps(data)

r=requests.post(url=URL,data=data)

dtar=r.json()

print(dtar)

