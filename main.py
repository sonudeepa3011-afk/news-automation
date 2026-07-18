from newsdata import get_latest_news
from gemini_ai import write_article

def main():
    try:
        news = get_latest_news()

        title = news.get("title", "")
        description = news.get("description", "")

        print("=" * 50)
        print("LATEST NEWS")
        print("=" * 50)

        print(title)
        print()

        print("Generating Article with Gemini AI...")
        print()

        article = write_article(title, description)

        print(article)

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()
