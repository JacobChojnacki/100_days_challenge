import requests
from datetime import datetime
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def iss_position_checker():
    if (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5) and (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().time().hour

while True:
    if iss_position_checker() and sunrise <= time_now <= sunset:
        print("Wyslij email")
    else:
        print("Nie wysylaj")
    time.sleep(60)
