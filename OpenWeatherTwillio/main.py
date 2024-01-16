from twilio.rest import Client
import requests

# CONSTANTS ------------------------------------------------------------------------------------------------------------
PARAMS_WEATHER = {
    "appid": "4abb9758bd25866549e0702978420e03",
    "lat": 19.432608,
    "lon": -99.133208,
    "exclude": "current,daily,minutely,daily,alerts",
}
API_WEATHER = "https://api.openweathermap.org/data/2.5/onecall"

ACC_SID = 'AC3d4b93aac8d9881196fdb269d85f91b6'
AUTH_TKN = '1d2eaf9e41c06538f0540a1b586e33a9'

# ----------------------------------------------------------------------------------------------------------------------
response_weather = requests.get(url=API_WEATHER, params=PARAMS_WEATHER)
response_weather.raise_for_status()
data = response_weather.json()

weather_12hrs = data['hourly'][:13]

id_data = [n['weather'][0]['id'] for n in weather_12hrs]
will_rain = False

for n in id_data:
    if n < 600:
        will_rain = True

if will_rain:
    client = Client(ACC_SID, AUTH_TKN)
    message = client.messages \
        .create(
            body="It is going to rain today, don't forget the umbrella",
            from_='+18593764065',
            to='+525578740735'
        )
    print(message.status)
