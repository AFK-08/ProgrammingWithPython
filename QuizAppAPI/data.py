import requests

parameters={
    "amount":10,
    "type":"boolean"
}
response = requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
content = response.json()

question_data = content["results"]
