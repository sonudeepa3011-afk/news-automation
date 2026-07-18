import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def write_article(title, description=""):
    prompt = f"""
You are a professional news journalist.

Write a unique SEO-friendly news article in HTML.

News Title:
{title}

Description:
{description}

Requirements:
- 300 to 400 words
- H2 and H3 headings
- Short paragraphs
- Human writing style
- No markdown
- End with conclusion
"""

    response = client.models.generate_content(
       model="gemini-2.0-flash-lite",
        contents=prompt
    )

    return response.text

import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for model in client.models.list():
    print(model.name)
