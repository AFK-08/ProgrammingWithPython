import requests
import os

## Exercise Calculator API
EXERCISE_API = "nix_live_YwwaY9B8HPU1aqmDSTS9WIigqWP69fEi"
X_APP_ID = "app_9c220284d4724bd380bb2fb7"

## Acessing date and time
from datetime import datetime
date = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%X")

## Sheety API and Headers for Authorization:
sheety_post_endpoint = "https://api.sheety.co/cfe2f857318f60093230f0fd8fa98b22/workoutTracking/workouts"

sheety_headers = {"Authorization": "Bearer ABCDEFGHI123456789"}

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_parameters = {
    "query": input("Which exercises you did: "),
}

headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": EXERCISE_API,
}

## Generating Response from Exercise API NLP

response = requests.post(url=exercise_endpoint,json=exercise_parameters,headers=headers)
data = response.json()

calories = data["exercises"][0]["nf_calories"]
duration = data["exercises"][0]["duration_min"]
Exercise_name = data["exercises"][0]["name"].title()

## Adding Records via Sheety API

workout_parameters = {
    "workout":{
        "date": date,
        "time" : time,
        "exercise" : Exercise_name,
        "duration": duration,
        "calories": calories,
    }
}

response = requests.post(url=sheety_post_endpoint,json=workout_parameters,headers=sheety_headers)

print(response.text)
