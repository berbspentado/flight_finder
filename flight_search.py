import requests
import os


AMADEUS_API_KEY = os.environ.get('AMADEUS_API_KEY')
AMADEUS_APK_SECRET = os.environ.get('AMADEUS_APK_SECRET')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.api_key = AMADEUS_API_KEY
        self.apk_secret = AMADEUS_APK_SECRET
        self.amadaeus_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            }
        self.amadeus_parameters={
            'grant_type':"client_credentials",
            'client_id':AMADEUS_API_KEY,
            'client_secret':AMADEUS_APK_SECRET,
            
        }
        

    def request_access_token(self):
        response = requests.post(url=self.amadaeus_endpoint, headers=self.headers, data=self.amadeus_parameters)
     
        print(response.text)
        