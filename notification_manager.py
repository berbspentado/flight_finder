from twilio.rest import Client
import os

TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        pass

    def send_notification(self,price_sms,iata_sms,departure_date):
        client = Client(ACCOUNT_SID, TWILIO_TOKEN)
        message = client.messages.create(
        body=f"Low price alert! Only ${price_sms} to {iata_sms} with departure date {departure_date}",
        from_="+12000000000", #DUMMY NUMBER
        to="+63000000000", #DUMMY NUMBER
        )
        print(message.status)
