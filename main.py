import os
import requests

NEWS_API = os.getenv("NEWSDATA_API_KEY")

url = f"https://newsdata.io/api/1/news?apikey={NEWS_API}&country=in&language=en"

response = requests.get(url)

print(response.status_code)
print(response.text[:500])
