import os
import requests
from seo import generate_meta_description

WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")


def create_draft(title, content):
    """
    Create WordPress Draft Post
    """

    meta_description = generate_meta_description(title, content)

    url = f"{WP_URL}/wp-json/wp/v2/posts"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "title": title,
        "content": content,
        "status": "draft",
        "excerpt": meta_description
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        auth=(WP_USERNAME, WP_APP_PASSWORD)
    )

    if response.status_code in [200, 201]:
        print("Draft Created Successfully!")
        return response.json()

    print("Error Creating Draft")
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    raise Exception("WordPress Draft Creation Failed")
