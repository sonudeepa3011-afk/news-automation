import requests
import os

WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")


def is_duplicate(title):
    url = f"{WP_URL}/wp-json/wp/v2/posts"

    response = requests.get(
        url,
        params={
            "search": title,
            "per_page": 5,
            "status": "draft,publish"
        },
        auth=(WP_USERNAME, WP_APP_PASSWORD)
    )

    if response.status_code != 200:
        return False

    posts = response.json()

    for post in posts:
        if post["title"]["rendered"].strip().lower() == title.strip().lower():
            return True

    return False
