# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
flight_data = data_manager.get_data_from_sheet()
flight_search = FlightSearch()
SMS = NotificationManager()
ORIGINAL_CITY = "WAW"

if flight_data[0]["iataCode"] == "":
    for row in flight_data:
        row["iataCode"] = flight_search.destination_code(row["city"])
    data_manager.flight_data = flight_data
    data_manager.update_iataCode()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(6 * 30))

for place in flight_data:
    flight = flight_search.search_flight(
        fly_from=ORIGINAL_CITY,
        fly_to=place["iataCode"],
        date_from=tomorrow,
        date_to=six_month_from_now,
    )
    try:
        if flight.price < place["lowestPrice"]:
            SMS.send_message(
                message=f"Low price alert! Only {flight.price} GBP to fly from\n"
                        f"{flight.origin_city}-{flight.origin_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport},\n "
                        f"from {flight.out_date} to {flight.return_date}")
    except AttributeError:
        continue
