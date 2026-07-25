api_key = "79d31498d34716250c4f430724523595"
import requests

parameters = {
    "lat":29.5368,
    "lon":71.6305,
    "appid":api_key,
    "cnt":4,
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()

for index in range(0,3):
    code = weather_data["list"][index]["weather"][0]["id"]
    if code<700:
        print("Bring an Umbrella")
        break

if code > 700:
     print("Everything is fine!")



