import requests
sheety_get_endpoint = "https://api.sheety.co/cfe2f857318f60093230f0fd8fa98b22/flightDeals/prices"

class DataManager:
    def get_data(self):
        response = requests.get(url=sheety_get_endpoint)
        self.sheet_data = response.json()
        return self.sheet_data["prices"]
