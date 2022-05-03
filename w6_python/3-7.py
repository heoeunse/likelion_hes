import requests
import json

city = "Seoul"
apikey = "8a4c79367e4c59cd9aba3e6aaee0cbb1"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)
print(type(result.text))
print(type(data))