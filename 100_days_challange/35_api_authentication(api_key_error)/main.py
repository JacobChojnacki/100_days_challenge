import requests

API_KEY = "f60ac934cd1edf1121952ca050cb2c5d"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": 51.919437,
    "lon": 19.145136,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
