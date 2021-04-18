import requests
import json


r = requests.post(url='http://127.0.0.1:8800/hello', json={'name': '叶青照'})
print(r.json())