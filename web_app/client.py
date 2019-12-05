import json
import requests

url = 'http://localhost:5000/'

data = {'text': 'boh'}
request = requests.post(url, json=json.dumps(data))

print(request.text)