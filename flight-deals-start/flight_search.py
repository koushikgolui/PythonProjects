import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.KIWI_LOCATIONS_API = "https://tequila-api.kiwi.com/locations/query"
        self.headers = {
            "apikey": "b7_LRfi0UUA1BezS2pUHAmwnlAf3QKiw"
        }

    def get_iata_codes(self, city):
        search_data = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=self.KIWI_LOCATIONS_API, params=search_data, headers=self.headers)
        return response.json()["locations"][0]["code"]



