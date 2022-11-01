import requests
import datetime
from requests.auth import HTTPBasicAuth

API_ID = ""
API_KEY = ""
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/49865048ff9c3af97022055234a76f1f/exerciseTracking/workouts"
# users params
QUERY = input("Tell me which exercises you did: ")
GENDER = "male"
WEIGHT_KM = 75.0
HEIGHT_CM = 172.50
AGE = 23

exercise_params = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KM,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": API_ID,
    'x-app-key': API_KEY,
}

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%X")

response = requests.post(url, json=exercise_params, headers=headers)
filtered_response = response.json()["exercises"]
basic = HTTPBasicAuth("user", "password")

for exercise in filtered_response:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheety_url, json=sheet_input, auth=basic)
