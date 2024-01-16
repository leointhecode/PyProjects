import requests
from data_manager import data_list
from datetime import datetime

today = datetime.now()

URL = "https://tequila-api.kiwi.com/v2/search"
API_KEY = "knhBGZWTsE9NuYgdiBu_MP4yxJlQjAXb"

parameters = {
    "fly_from": "MEX",
    "date_from": today.strftime("%d/%m/%Y"),
    "date_to": f"31/12/{today.year + 1}",
    "curr": "MXN",
    "one_for_city": 1,
    "locale": "en"
}
headers = {"apikey": API_KEY}


class FlightSearch:

    def __init__(self):
        self.deals = requests.get(url=URL, headers=headers, params=parameters).json()

    def best_deal(self):
        new_data = []
        for n in data_list:
            for j in self.deals['data']:
                if n['city'] in j['cityTo']:
                    data = {
                        "city": j['cityTo'],
                        "iataCode": j['flyTo'],
                        "lowestPrice": j['price'],
                        "arrival": j['local_arrival'],
                        "departure": j['local_departure']
                    }

                    new_data.append(data)
        return new_data
