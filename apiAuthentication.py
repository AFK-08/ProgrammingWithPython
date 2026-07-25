api_key = "79d31498d34716250c4f430724523595"

import requests

parameters={
    "lat":29.5368,
    "lon":71.6305,
    "appid":api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather",params=parameters)
response.raise_for_status()
data = response.json()
print(data)



