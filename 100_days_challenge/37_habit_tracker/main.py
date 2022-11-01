import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "7ea0b415bbcf43c5b7938e892ad2c949"
USERNAME = "jacobian"

users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

pixela_create_graph = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"

graph_config = {
    "id": graph_id,
    "name": "ML Graph",
    "unit": "H",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_create_graph, json=graph_config, headers=headers)
# print(response.text)
pixel_config = {
    "date": str(datetime.date.today()).replace("-", ""),
    "quantity": "8"
}

# pixela_post_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
# response = requests.post(url=pixela_post_pixel, json=pixel_config, headers=headers)
# print(response.text)
