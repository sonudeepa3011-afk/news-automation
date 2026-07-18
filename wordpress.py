import os
import requests

WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")


def create_draft(title, article, meta_description, comma_tags):
    """
    Create WordPress Draft
    """

    final_content = f"""
{article}

<hr>

<h2>SEO Details</h2>

<p><strong>Meta Description:</strong></p>
<p>{meta_description}</p>

<br>

<p><strong>Comma Tags:</strong></p>
<p>{comma_tags}</p>
"""

    data = {
        "title": title,
        "content": final_content,
        "status": "draft"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{WP_URL}/wp-json/wp/v2/posts",
        headers=headers,
        json=data,
        auth=(WP_USERNAME, WP_APP_PASSWORD)
    )

    if response.status_code in [200, 201]:
        print("===================================")
        print("Draft Created Successfully!")
        print("Post ID :", response.json().get("id"))
        print("Post URL:", response.json().get("link"))
        print("===================================")
        return response.json()

    print("===================================")
    print("WordPress Error")
    print("Status Code:", response.status_code)
    print(response.text)
    print("===================================")

    raise Exception("Failed to create WordPress draft.")
