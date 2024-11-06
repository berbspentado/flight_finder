import requests
import os
import flight_data


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheety_api_key = os.environ.get('SHEETY_API_FLIGHT')
        self.sheety_endpoint = "https://api.sheety.co/719e26062f6797b5021b1760973cbe49/flightDeals/prices"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': os.environ.get('SHEETY_API_FLIGHT')
            }
        self.flight_deals = {
            "price":{
                "city":"",
                "iatacode":"",
                "lowestPrice":"",
                "id":0,
            }
        }
        self.destination_countries = []
        self.lowest_prices_list = []

    #comment out 200 quote sheety api
    def get_google_sheets(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.headers, json=self.flight_deals)   
        data_json = response.json()
        data_sheets = data_json["prices"]

        self.destination_countries = [country["city"] for country in data_sheets]
        print(self.destination_countries)
        return self.destination_countries

    #update iata codes in the google sheets
    def update_google_sheets_iata(self):
        obj = flight_data.FlightData()
        obj.getIata_Code()
        iata_codes = obj.iata_codes
        index = 2

        for iata_code in iata_codes:
            print(f"{iata_code} with {index} from update sheets")
            countries_iata ={
                "price":{
                    "iataCode":iata_code,
                
                }
            }
            
            sheety_endpoint_update = f"https://api.sheety.co/719e26062f6797b5021b1760973cbe49/flightDeals/prices/{index}"
            

            #comment out 200 quote sheety api
            response = requests.put(url=sheety_endpoint_update, headers=self.headers, json=countries_iata)
            response.raise_for_status()

            index+=1
            print(response.text)

    #get price google sheets
    def getPrice_google_sheets(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.headers, json=self.flight_deals)   
        data_json = response.json()
        data_sheets = data_json["prices"]

        self.lowest_prices_list = [prices["lowestPrice"] for prices in data_sheets]
        print(self.lowest_prices_list)

        return self.lowest_prices_list
   
        
