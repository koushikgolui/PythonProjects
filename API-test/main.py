import requests

api_key = "66ed6a7567e29e13fc7441e1b7181d09"

parameters = {
    "lat": 39.094640,
    "lon": -1.361150,
    "exclude": "current,minutely,daily",
    "units": "metric",
    "appid": api_key
}

# api.openweathermap.org/data/2.5/weather?lat=33.0198&lon=-96.698883&appid=66ed6a7567e29e13fc7441e1b7181d09

# api.openweathermap.org/data/2.5/weather?q=Plano,tx,US&appid=66ed6a7567e29e13fc7441e1b7181d09

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_12hour = weather_data["hourly"][0:12]

# weather_condition = []
# for weather in weather_12hour:
#     for condition in weather["weather"]:
#         if int(condition["id"]) < 700:
#             weather_condition.append(condition["id"])
weather_condition = [condition["id"] for weather in weather_12hour for condition in weather["weather"]
                     if int(condition["id"]) < 700]

if len(weather_condition) > 0:
    print("Bring Umbrella")

