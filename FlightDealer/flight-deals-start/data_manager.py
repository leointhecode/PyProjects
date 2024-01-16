import requests

SHEETY_URL = "https://api.sheety.co/f1e7ee83530ef69df98b60cad1df5b6e/flightDeals/prices"

SHEETY_URL_USER = "https://api.sheety.co/f1e7ee83530ef69df98b60cad1df5b6e/flightDeals/users"

SHEETY_headers = {
    "Authorization": "Bearer voenvioajbvleirbv;iwrj4518e4w#"
}

response = requests.get(url=SHEETY_URL, headers=SHEETY_headers)
data_list = response.json()['prices']

response_mail = requests.get(url=SHEETY_URL_USER, headers=SHEETY_headers)
email = response_mail.json()['users']
emails = [n['email'] for n in email]


class DataManager:
    def __init__(self, parameters: list, name="", l_name="", email=""):
        self.parameters = parameters
        self.params_user = {
            'user': {
                'firstName': name,
                'lastName': l_name,
                'email': email
            }
        }
        self.data_list = data_list

    def add_row(self):
        self.delete_all()
        for n in self.parameters:
            par = {'price': n}
            requests.post(url=SHEETY_URL, json=par, headers=SHEETY_headers)

    def add_user(self):
        requests.post(url=SHEETY_URL_USER, json=self.params_user, headers=SHEETY_headers)

    def delete_all(self):
        m = 2
        url = f"https://api.sheety.co/f1e7ee83530ef69df98b60cad1df5b6e/flightDeals/prices/{m}"
        for n in range(0, len(self.data_list)):
            requests.delete(url=url, headers=SHEETY_headers)
            m += 1
