import requests
from requests.auth import HTTPBasicAuth

SHEETY_URL = "https://api.sheety.co/49865048ff9c3af97022055234a76f1f/flightDealsChallenge/prices"
basic = HTTPBasicAuth(username="", password="")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_data = {}

    def get_data_from_sheet(self):
        self.flight_data = requests.get(url=SHEETY_URL, auth=basic).json()['prices']
        return self.flight_data

    def update_iataCode(self):
        for flight in self.flight_data:
            new_data = {
                "price": {
                    "iataCode": flight["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_URL}/{flight['id']}", json=new_data, auth=basic)
