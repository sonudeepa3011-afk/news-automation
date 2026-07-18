import requests
from bs4 import BeautifulSoup


URL = "https://avenuemail.in/"


def get_latest_news():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers, timeout=20)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    news_list = []

    # Homepage के सभी links निकालो
    links = soup.find_all("a", href=True)

    for link in links:

        title = link.get_text(strip=True)
        href = link["href"]

        if len(title) < 25:
            continue

        if not href.startswith("http"):
            continue

        news_list.append({
            "title": title,
            "url": href
        })

    # Duplicate हटाओ
    unique = []
    seen = set()

    for item in news_list:
        if item["url"] not in seen:
            seen.add(item["url"])
            unique.append(item)

    return unique[:10]
