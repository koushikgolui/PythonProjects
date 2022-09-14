from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
import requests
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


datamanager = DataManager()
flights = FlightSearch()
flight_price = FlightData()

sheet_data = datamanager.read_data_from_sheet()

fly_from = input("Where are you flying from? ")

for row in sheet_data:
    row_id = row["id"]
    city = row["city"]
    iatacode = row["iataCode"]
    if iatacode == "":
        iatacode = flights.get_iata_codes(city)
        datamanager.update_iata_code(row_id, iatacode)
    flight_price.get_lowest_price(fly_from, iatacode)

# thisday = datetime.today()
#
# date_from = datetime.strftime(thisday + timedelta(days=1), "%d/%m/%Y")
# date_to = datetime.strftime(thisday + timedelta(days=181), "%d/%m/%Y")
#
# print (f"{thisday}-{date_to}-{date_from}")


