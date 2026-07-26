## PIXELA API PIXELS GRAPH API

import requests

USERNAME = "ahmadfk"
TOKEN = "Abcd1234ghi"

## Creating User Account on Pixela API

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = "https://pixe.la/v1/users/ahmadfk/graphs"

graph_config = {
    "id":"graph1",
    "name": "Book Reading Tracker",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# response.raise_for_status()
# print(response.text)

pixels_endpoint = "https://pixe.la/v1/users/ahmadfk/graphs/graph1"

pixels_config= {
    "date": "20260726",
    "quantity": "8"
}

# response = requests.post(url=pixels_endpoint,json=pixels_config,headers=headers)
# print(response.text)

pixels_update = "https://pixe.la/v1/users/ahmadfk/graphs/graph1/20260726"
pixels_update_config = {
    "quantity": "8",
}

# response = requests.put(url=pixels_update,json=pixels_update_config,headers=headers)
# print(response.text)
