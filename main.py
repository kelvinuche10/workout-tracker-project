import requests
from datetime import datetime

APP_ID = '20dc56b4'
API_KEY = 'c19d81e2992340026e5e23c90bd570ec'

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/b24d40efccfe08788e5556a7c3725302/workoutsTracking/workouts'

headers = {
	'x-app-id': APP_ID,
	'x-app-key': API_KEY,
	'Content-Type': 'application/json'
}

sheety_header = {
	'Authorization': f'Basic {your_sheety_key}',
	'Content-Type': 'application/json'
}

query = input('Which exercise did you do today? ')
params = {
	'query': query,
	'gender': 'male',
	'weight_kg': '65',
	'height_cm': 183.33,
	'age': 35,
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)

date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%H/%M/%S')
for _ in response.json()['exercises']:
	sheety_params = {
		'workout': {
		'date': date,
		'time': time, 
		'exercise': _['name'],
		'duration': _['duration_min'],
		'calories': _['nf_calories'],
		}
		}

sheety_response = requests.post(url=sheety_endpoint, headers=sheety_header, json=sheety_params)
print(sheety_response.status_code)
