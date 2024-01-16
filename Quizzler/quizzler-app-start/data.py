import requests

parameters = {"amount": 10, "type": "boolean"}
response_quiz = requests.get(url="https://opentdb.com/api.php", params=parameters)
response_quiz.raise_for_status()

data = response_quiz.json()
question_data = data['results']
