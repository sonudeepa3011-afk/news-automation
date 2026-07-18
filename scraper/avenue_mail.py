import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://avenuemail.in/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_article_content(url):

    try:

        response = requests.get(url, headers=HEADERS, timeout=20)

        if response.status_code != 200:
            return ""

        soup = BeautifulSoup(response.text, "html.parser")

        article = (
            soup.find("div", class_="entry-content")
            or soup.find("article")
            or soup
        )

        paragraphs = article.find_all("p")

        content = []

        for p in paragraphs:

            text = p.get_text(" ", strip=True)

            if len(text) > 25:
                content.append(text)

        return "\n".join(content)

    except Exception as e:
        print("Article Error:", e)
        return ""


def get_latest_news():

    news = []

    try:

        response = requests.get(BASE_URL, headers=HEADERS, timeout=20)

        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        seen = set()

        articles = soup.find_all("article")

        today = datetime.now().strftime("%Y-%m-%d")

        for article in articles:

            h2 = article.find(["h2", "h3"])

            if not h2:
                continue

            a = h2.find("a")

            if not a:
                continue

            title = a.get_text(strip=True)
            url = a.get("href")

            if not url:
                continue

            if url in seen:
                continue

            seen.add(url)

            content = get_article_content(url)

            if len(content) < 100:
                continue

            news.append({
                "title": title,
                "content": content,
                "description": content[:500],
                "url": url,
                "date": today
            })

            if len(news) >= 10:
                break

    except Exception as e:
        print("Avenue Mail Error:", e)

    return news
