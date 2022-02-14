import json
import urllib
import wave
token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZW4iLCJleHAiOjE2NDQ4Njk4NjZ9.HfI93bUFks5uLpyv9ppJ9su4ONePJxVar9aNCVuPL-Y'


import requests
# res = requests.get('https://www.youtube.com/watch?v=RyZ4RuCUiQw')
# ress = str(res.text).split('{"itag":251,')[1].split(',"mimeType"')
# ress = ('{' + ress[0] + '}')
# ress = json.loads(ress)
# url1 = urllib.parse.unquote(ress['url'])
# print(url1)
# url2 = urllib.parse.unquote(ress['url'])+'&range=200000-400000'
# cont1 = requests.get(url1, headers={'Youtubedl-no-compression': 'True'}).content

# req = requests.get(url, )

# open the file for reading.


# open stream based on the wave object which has been input.

r = requests.get('http://127.0.0.1:8080/users/den', headers={'Authorization': 'Bearer ' + token})
print(r.json())





