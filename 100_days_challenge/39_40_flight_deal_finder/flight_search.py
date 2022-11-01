import requests
from flight_data import FlightData


url = "https://api.tequila.kiwi.com/locations/query"
url_search = "https://api.tequila.kiwi.com/v2/search"
apikey = ""


class FlightSearch:
    def __init__(self):
        self.headers = {"apikey": apikey}

    # This class is responsible for talking to the Flight Search API.
    def destination_code(self, city_name):
        query_params = {"term": city_name,
                        "lacation_types": "city"}
        response = requests.get(url=url, headers=self.headers, params=query_params).json()['locations']
        return response[0]["code"]

    def search_flight(self, fly_from, fly_to, date_from, date_to):
        search_params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=url_search, headers=self.headers, params=search_params)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights")
            return "No flights"
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
