EXERCISE_API = "nix_live_YwwaY9B8HPU1aqmDSTS9WIigqWP69fEi"
X_APP_ID = "app_9c220284d4724bd380bb2fb7"
import requests

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_parameters = {
    "query": input("Which exercises you did: "),
}

headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": EXERCISE_API,
}


response = requests.post(url=exercise_endpoint,json=exercise_parameters,headers=headers)
data = response.json()
print(data["exercises"][0]["nf_calories"])


