import requests
import datetime
from twilio.rest import Client

API_KEY_STAGE1 = ""
API_KEY_STAGE2 = ""
API_KEY_TWILIO = ""
API_AUTH_TOKEN_TWILIO = ""
to_phone_number = ""
from_phone_number = ""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
BEFORE_YESTERDAY = datetime.date.today().replace(day=datetime.date.today().day - 2)
YESTERDAY = datetime.date.today().replace(day=datetime.date.today().day - 1)

functions = {
    "symbol": STOCK,
    "apikey": API_KEY_STAGE1,
    "function": "TIME_SERIES_DAILY",
    "datetype": "json"
}
functions_stage_2 = {
    "q": COMPANY_NAME,
    "from": datetime.date.today(),
    "sortBy": "popularity",
    "apiKey": API_KEY_STAGE2
}

url = f'https://www.alphavantage.co/query'
url_stage_2 = "https://newsapi.org/v2/everything"

response = requests.get(url, params=functions)
response_stage_2 = requests.get(url_stage_2, params=functions_stage_2)

yesterday_data = response.json()["Time Series (Daily)"][f"{YESTERDAY}"]["4. close"]
before_yesterday = response.json()["Time Series (Daily)"][f"{BEFORE_YESTERDAY}"]["4. close"]

difference = float(yesterday_data) - float(before_yesterday)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

difference_percentage = round((difference / float(yesterday_data)) * 100, 2)

if abs(difference_percentage) < 5:
    articles = response_stage_2.json()["articles"][:3]

    sms_data = [
        f"{STOCK}: {up_down}{difference_percentage}% \nHeadline: {item['title']}. \nBrief: {item['description']}" for
        item in articles]
    client = Client(API_KEY_TWILIO, API_AUTH_TOKEN_TWILIO)

    for article in sms_data:
        message = client.messages.create(
            body=article,
            from_=from_phone_number,
            to=to_phone_number
        )
