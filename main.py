import requests
from datetime import datetime
import os

GENDER = "MALE"
WEIGHT_KG = 72.57
HEIGHT_CM = 182.88
AGE = 19


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
add_row_endpoint = os.environ["ADD_ROW_ENDPOINT"]


workout_input = input("Tell me which exercise you did:")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

user_info = {
    "query": workout_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=user_info, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%Y-%m-%d")
now_time = datetime.now().strftime("%X")


bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}


for exercise in result["exercises"]:
    exercise_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }

    }

sheet_response = requests.post(url=add_row_endpoint, json=exercise_input, headers=bearer_headers)
print(sheet_response.text)
