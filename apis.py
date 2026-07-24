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


