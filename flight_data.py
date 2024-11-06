import requests
import data_manager
import notification_manager
# "access_token": "biqBMmhAh8f8EugXm42a4UURoGn7"

HEADERS ={
    "Authorization": "Bearer biqBMmhAh8f8EugXm42a4UURoGn7"
}


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.iata_codes = []
        self.lowest_prices_country = {}

    #get the iata code of the countries listed in the google sheets
    def getIata_Code(self):
        #comment out 200 quote sheety api
        countries = data_manager.DataManager()
        # countries = ["Paris","Frankfurt","Tokyo","Hong Kong","Istanbul","Kuala Lumpur","New York","San Francisco","Dublin"]
        get_iata_codes_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
       
        #comment out 200 quote sheety api
        for country in countries.get_google_sheets():
        # for country in countries:
            params = {
                    "keyword": country,
                }

            response = requests.get(url=get_iata_codes_endpoint, params=params,headers=HEADERS)
            data_json = response.json()
            

            iata_code = data_json['data'][0]['iataCode']
            print(iata_code)
            self.iata_codes.append(iata_code)

            
        print(self.iata_codes)
        return self.iata_codes
            
    
    #get details for flight based on the list countries in the sheets
    def get_flight_details(self):
        notification_sms = notification_manager.NotificationManager()
        self.lists_to_dictionary()
        flight_data_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
       
        for iata_code, prices in self.lowest_prices_country.items():
            parameters ={
                "originLocationCode":"BOS",
                "destinationLocationCode": {iata_code},
                "departureDate": "2025-01-14",
                "adults":2,
                "maxPrice":1000,
                "max":2,
                'currencyCode':"USD",
            }

            response=requests.get(url=flight_data_endpoint,headers=HEADERS, params=parameters)
            data_json = response.json()
            # print(data_json['data'])

            for country in data_json['data']:
                total_price = country["price"]["total"]
                arrival = [x['segments'][0]['arrival']['iataCode'] for x in country['itineraries']]

                if float(total_price) < float(prices):
                    print(f"{country['price']['total']} flight time diri, sa sheets ang price kay {prices}")
                    print(f"Low price alert! Only ${total_price} to {arrival}, with departure date {parameters['departureDate']}")

                    notification_sms.send_notification(total_price,arrival,parameters['departureDate'])
            

            # for country in data_json['data']:
            #     total_price = country["price"]["total"]
            #     if float(country["price"]["total"]) < float(prices):
            #         print(f"{country['price']['total']} flight time diri, sa sheets ang price kay {prices}")
            #         notification_sms.send_notification(total_price,"IAO")
            #     else:
            #         print(f"puyo sa kay sa sheets {prices} nya sa amadeus kay {country['price']['total']}")
                

    #get lowest price from the sheets inside DataManager object
    def getLowest_Price(self):
        obj = data_manager.DataManager()
        obj.getPrice_google_sheets()

        return obj.lowest_prices_list
    

    #makign the lists into dictionary
    # comment out api sheety 200 requests per month only
    def lists_to_dictionary(self):
        # iata_codes = self.getIata_Code()
        # lowest_price = self.getLowest_Price()

        iata_codes = ['PAR', 'FRA', 'TYO', 'HKG', 'IST', 'KUL', 'NYC', 'SFO', 'DBN']
        lowest_price = [1000, 500, 485, 551, 1000, 414, 240, 260, 378]

        for key in iata_codes:
            for val in lowest_price:
                self.lowest_prices_country[key] = val
                lowest_price.remove(val)
                break

        print(self.lowest_prices_country)           
        return self.lowest_prices_country
        

