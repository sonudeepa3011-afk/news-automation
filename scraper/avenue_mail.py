import requests
from bs4 import BeautifulSoup

BASE_URL = "https://avenuemail.in/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_article_content(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=20)

        if response.status_code != 200:
            return ""

        soup = BeautifulSoup(response.text, "lxml")

        paragraphs = soup.find_all("p")

        content = []

        for p in paragraphs:
            text = p.get_text(" ", strip=True)

            if len(text) > 40:
                content.append(text)

        return "\n".join(content)

    except Exception as e:
        print("Article Error:", e)
        return ""


def get_latest_news():

    try:

        response = requests.get(BASE_URL, headers=HEADERS, timeout=20)

        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "lxml")

        news = []
        seen = set()

        for a in soup.find_all("a", href=True):

            title = a.get_text(" ", strip=True)
            url = a["href"]

            if not url.startswith("http"):
                continue

            if len(title) < 25:
                continue

            if url in seen:
                continue

            seen.add(url)

            print("Reading:", title)

            article = get_article_content(url)

            if len(article) < 100:
                continue

            news.append({
                "title": title,
                "description": article[:500],
                "content": article,
                "url": url
            })

            if len(news) == 10:
                break

        return news

    except Exception as e:
        print("Homepage Error:", e)
        return []
