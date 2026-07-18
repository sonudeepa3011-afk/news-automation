import os
import requests

api_key = os.getenv("NEWSDATA_API_KEY")

url = f"https://newsdata.io/api/1/news?apikey={api_key}&country=in&language=en"

response = requests.get(url)

print("Status:", response.status_code)

data = response.json()

if "results" in data and len(data["results"]) > 0:
    news = data["results"][0]
    print("Title:", news.get("title"))
    print("Source:", news.get("source_name"))
    print("Link:", news.get("link"))
else:
    print(data)
