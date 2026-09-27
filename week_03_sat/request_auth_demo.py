import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("NEWSAPI_KEY")
# print(api_key)

response = requests.get(
    "https://newsapi.org/v2/top-headlines",
    params={"country": "us", "category": "technology"},
    headers={"X-Api-Key": api_key},
)

data = response.json()
print(data)
for article in data.get("articles", [])[:3]:
    print(article["title"])