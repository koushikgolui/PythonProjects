from datetime import datetime, timedelta
import requests


class FlightData:

    def __init__(self):
        self.KIWI_SEARCH_API = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {
            "apikey": ""
        }
        self.today = datetime.today()

    def get_lowest_price(self, fly_from, fly_to):
        date_from = datetime.strftime(self.today + timedelta(days=1), "%d/%m/%Y")
        date_to = datetime.strftime(self.today + timedelta(days=181), "%d/%m/%Y")
        search_parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0,
            "limit": 10
        }

        response = requests.get(url=self.KIWI_SEARCH_API, params=search_parameters, headers=self.headers)
        lowest_price_result = response.json()["data"][0]

        fly_from_airport = lowest_price_result["flyFrom"]
        fly_to_airport = lowest_price_result["flyTo"]
        flight_price = lowest_price_result["price"]
        # date_departure = lowest_price_result
        print(f"{fly_from}-{fly_from_airport} to {fly_to}-{fly_to_airport} from GBP{flight_price}")





    #This class is responsible for structuring the flight data.
