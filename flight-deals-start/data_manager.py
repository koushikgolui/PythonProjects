import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_API = "https://api.sheety.co/274d7904adbee5f514c9e43b03e93fe1/flightDeals/prices"
        self.AUTHORIZATION_KEY = {
            "Authorization": "Bearer apowers@007"
        }

    def read_data_from_sheet(self):
        response = requests.get(url=self.SHEETY_API, headers=self.AUTHORIZATION_KEY)
        # print(response.text)
        return response.json()['prices']

    def update_iata_code(self, rowid, iatacode):
        data = {
            "price":
            {
            "iataCode": iatacode
            }
        }
        response = requests.put(url=f"{self.SHEETY_API}/{rowid}", json=data, headers=self.AUTHORIZATION_KEY)
        # print(response.text)
