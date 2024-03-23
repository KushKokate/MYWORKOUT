import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 19


APP_ID = "3fb3ac02"
API_KEY = "f3eb209fd5360ef39328a1ff6398c19a	"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/4ee973ff7ebca45d7aaab62454d98841/workoutTracking/workouts"
exercise_output = input("What exercise did you do ? ")
parameters = {
    "query":exercise_output,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}
headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
############ SHEETY API #################
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url = sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)