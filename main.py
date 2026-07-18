from newsdata import get_latest_news
from gemini_ai import write_article
from wordpress import create_draft

def main():
    try:
        news = get_latest_news()

        title = news.get("title", "Untitled News")
        description = news.get("description", "")

        print(f"News: {title}")

        print("Generating article...")
        article = write_article(title, description)

        print("Creating WordPress draft...")
        result = create_draft(title, article)

        print("Draft Created Successfully!")
        print("Post ID:", result.get("id"))
        print("Post URL:", result.get("link"))

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()
