from pathlib import Path
from dotenv import load_dotenv
import os 
import requests

# Finds the .env file in the exact same directory as this script

dotenv_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

## Open Weather API keys and Parameters:

api_key = "79d31498d34716250c4f430724523595"
parameters = {
    "lat":29.5368,
    "lon":71.6305,
    "appid":api_key,
    "cnt":4,
}

## Twilio: 
account_sid = os.environ.get("ACCOUNT_SID_TWILIO")
auth_token = os.environ.get("AUTH_TOKEN_TWILIO")
from twilio.rest import Client

## Accessing Weather codes:

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()
for index in range(0,3):

    code = weather_data["list"][index]["weather"][0]["id"]

    if int(code)<700:
        break

if int(code)>700:
    message = "Ahmad! The Sky is Clear Today. Kill today."
else:
    message = "There is going to be Rain Today Ahmad!"

## Sending SMS using Twilio:

client = Client(account_sid, auth_token)
message = client.messages.create(
         from_='whatsapp:+14155238886',
    
        body=message,
            
        to='whatsapp:+923044952492'
)
print(message.status)


    
    



