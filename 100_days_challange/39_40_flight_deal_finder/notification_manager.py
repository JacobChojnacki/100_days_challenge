from twilio.rest import Client

auth_id = ""
auth_token = ""


class NotificationManager():
    def __init__(self, ):
        self.client = Client(auth_id, auth_token)

    def send_message(self, message):
        self.client.messages.create \
            (body=message,
             from_="",
             to="")
