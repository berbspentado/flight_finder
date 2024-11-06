from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


# check_price2 = DataManager()
# check_price2.check()

# #0
access_token = FlightSearch()
access_token.request_access_token()

# 1
# update_iata_sheets = DataManager()
# update_iata_sheets.update_google_sheets_iata()

# 2
# get_price_sheets = DataManager()
# get_price_sheets.getPrice_google_sheets()

# 3
# dictionary_list = FlightData()
# dictionary_list.lists_to_dictionary()

# 4
flight_offers = FlightData()
flight_offers.get_flight_details()

# 5
send_notification = NotificationManager()
send_notification.send_notification()