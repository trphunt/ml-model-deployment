import json
import requests

url = 'http://42269d1f2d9c.ngrok.io/predict'

request_data = json.dumps({'age':42, 'salary':50000})
response = requests.post(url, request_data)
print (response.text)
