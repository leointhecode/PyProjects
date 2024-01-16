import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "vn0[eirn03ir2mpa2"
USERNAME = "touchmelenny"

user_parameters = {
    "token": "vn0[eirn03ir2mpa2",
    "username": "touchmelenny",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_parameters)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": "lennyofmiko8",
    "name": "language graph",
    "unit": "units",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)

today = datetime.datetime.now()

add_pixel_endpoint = f"{graph_endpoint}/{graph_parameters['id']}"

add_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

# response = requests.post(url=add_pixel_endpoint, json=add_pixel, headers=headers)

update_endpoint = f"{add_pixel_endpoint}/{add_pixel['date']}"

update_params = {
    "quantity": "10"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)

delete_endpoint = update_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)

print(response.text)


