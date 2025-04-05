import requests

API_URL = "http://localhost:3965/api/v1/prediction/9802ddb0-e43d-4b3f-8b26-cc10b6e4f4f2"


def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()


questions = [
    "請問四月份在麥當勞總共消費了多少錢?",
    "請問四月份最高的單筆消費是?",
]

output = query({"question": questions[1]})
print(output)
