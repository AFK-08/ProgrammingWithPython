## APIS is a set of commands, rules or protocols to create a software or interact with the external system.

## Making 1st API request to ISS

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
