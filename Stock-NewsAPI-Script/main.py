STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
from dotenv import load_dotenv
from pathlib import Path

import requests,os
account_sid = os.environ.get("ACCOUNT_SID_TWILIO")
auth_token = os.environ.get("AUTH_TOKEN_TWILIO")
from twilio.rest import Client


# Finds the .env file in the exact same directory as this script
dotenv_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

## Stock API Parameters:
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("STOCK_API"),
}
response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
response.raise_for_status()
data = response.json()
data = data["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
## Calculating Price Difference:

yesterday_price = float(data_list[0]["4. close"])
before_yesterday = float(data_list[1]["4. close"])

if yesterday_price>before_yesterday:
    price_difference  = yesterday_price - before_yesterday
    percentage = price_difference/before_yesterday*100
    message = f"Stock price increases {percentage}%"
    print(message)

elif yesterday_price<before_yesterday:
    price_difference  = before_yesterday- yesterday_price
    percentage = price_difference/before_yesterday*100
    percentage = round(percentage,2)
    message = f"Stock price decreases {percentage}%"
    print(message)


news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": os.environ.get("STOCK_API"),
}
response = requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
response.raise_for_status()
news_data = response.json()
articles = news_data["articles"]
three_articles = articles[:3]
formatted_article = [f"Headline: {article['title']}\n Description: {article['description']}" for article in three_articles]

print(formatted_article)

## Twilio: 
## Sending SMS using Twilio:
for article in formatted_article:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            from_='whatsapp:+14155238886',
        
            body=f"{message}\n{article}",
                
            to='whatsapp:+923044952492'
    )
    print(message.status)

