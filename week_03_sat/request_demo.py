import requests


# response = requests.get("https://api.github.com/users/cvzxcvzs") #public API

# print(response.status_code)
# data = response.json()
# print(data)
# print(f"Name: {data['name']}")
# print(f"Bio: {data['bio']}")
# print(f"Public repos: {data['public_repos']}")
# print(f"Followers: {data['followers']:,}")

# OPENAI - 
# gives you token - $20 - particular limit

# call an API via python - 
# free account - limited

# UI profile -> API_token - asdlfhasldfhqoweuhour123412341234b - 401 - private API


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 19.0760,    # Mumbai
    "longitude": 72.8777,
    "current_weather": True,
}
response = requests.get(url, params=params)
data = response.json()
print(f"Temperature in Mumbai: {data['current_weather']['temperature']}°C")


# API = a way for one program to ask another program for data
# GET = "give me something"
# JSON = "a Python dict pretending to be a string"
# Status codes: 200 good, 404 not found, 500 server broke, 401 Unauth