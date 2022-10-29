import requests
from requests.auth import HTTPBasicAuth

SHEETY_URL_GET = 'https://api.sheety.co/49865048ff9c3af97022055234a76f1f/flightDealsChallenge/prices'
USER = "jacob"
PASSWORD = "flightchallenge"

basic = HTTPBasicAuth(USER, PASSWORD)


class DataManager:
    pass