## APIS is a set of commands, rules or protocols to create a software or interact with the external system.

## Making 1st API request to ISS

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

## Making more specifc by entering into json
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude,latitude)
print(iss_position)

parameters = {
    "lat":29.506624,
    "lng":71.635917,
    "formatted":0,
}

## Making 2nd SUNRISE AND SUNSET TIME API

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)

response.raise_for_status()
data = response.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]


print(sunrise_time)
print(sunset_time)

