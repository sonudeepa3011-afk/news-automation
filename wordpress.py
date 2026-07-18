import os
import requests

def create_draft(title, content):
    url = os.getenv("WP_URL") + "/wp-json/wp/v2/posts"

    username = os.getenv("WP_USERNAME")
    password = os.getenv("WP_APP_PASSWORD")

    response = requests.post(
        url,
        auth=(username, password),
        json={
            "title": title,
            "content": content,
            "status": "draft"
        },
        timeout=30
    )

    if response.status_code not in (200, 201):
        raise Exception(
            f"WordPress Error: {response.status_code} - {response.text}"
        )

    return response.json()
