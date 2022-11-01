import requests
from requests.auth import HTTPBasicAuth

SHEETY_URL = "https://api.sheety.co/49865048ff9c3af97022055234a76f1f/flightDealsChallenge/prices"
SHEETY_URL_USERS = "https://api.sheety.co/49865048ff9c3af97022055234a76f1f/flightDealsChallenge/users/"
basic = HTTPBasicAuth(username="", password="")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_data = {}
        self.users = {}

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

    def get_users_from_sheet(self):
        self.users = requests.get(url=SHEETY_URL_USERS, auth=basic).json()["users"]
        return self.users

    def add_user(self):
        name = input("What is your first name?\n")
        lastName = input("What is your last name?\n")
        email = input("What is your email?\n")
        body = {
            "user": {
                "firstName": name,
                "lastName": lastName,
                "email": email
            }
        }
        requests.put(url=f"{SHEETY_URL_USERS}/{len(self.users) + 2}", json=body, auth=basic)
