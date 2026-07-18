import requests
import os

WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")


def is_duplicate(title, slug):
    url = f"{WP_URL}/wp-json/wp/v2/posts"

    response = requests.get(
        url,
        params={
            "search": slug,
            "per_page": 10,
            "status": "draft,publish"
        },
        auth=(WP_USERNAME, WP_APP_PASSWORD),
        timeout=20
    )

    if response.status_code != 200:
        return False

    posts = response.json()

    title = title.strip().lower()

    for post in posts:

        wp_title = post["title"]["rendered"].strip().lower()

        if wp_title == title:
            return True

        if slug == post["slug"]:
            return True

    return False
