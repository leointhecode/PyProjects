import requests
from datetime import *

NUTRITION_APP_ID = "9f6ecdd7"
NUTRITION_API_KEY = "57d1c51ef15a9487d4938f5ce920d906"
NUTRITION_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_URL = "https://api.sheety.co/f1e7ee83530ef69df98b60cad1df5b6e/workoutTraining/workouts"

SHEETY_headers = {
    "Authorization": "Bearer VWPI@EJ&RVPO*EAJoj%%cdevi#ewjjfebvewifni54-32"
}

NUTRITION_headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}

NUTRITION_parameters = {
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 183,
    "age": 18,
    "query": input("How did you worked out today? ")
}

nutrition_response = requests.post(url=NUTRITION_URL, json=NUTRITION_parameters, headers=NUTRITION_headers)
data = nutrition_response.json()
print(data)
today = datetime.now()

exercise_name = data['exercises'][0]['user_input']
exercise_duration = data['exercises'][0]['duration_min']
calories_burned = data['exercises'][0]['nf_calories']

SHEETY_parameters = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%I:%M:%S"),
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": calories_burned,
    }
}

sheety_response = requests.post(url=SHEETY_URL, json=SHEETY_parameters, headers=SHEETY_headers)
sheety_response.raise_for_status()
