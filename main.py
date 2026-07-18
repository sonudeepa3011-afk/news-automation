from newsdata import get_latest_news
from gemini_ai import write_article
from wordpress import create_draft
from duplicate import is_duplicate


def main():
    try:
        # Get latest news
        news = get_latest_news()

        title = news.get("title", "Untitled News")
        description = news.get("description", "")

        print(f"News Title: {title}")

        # Check duplicate
        if is_duplicate(title):
            print("Duplicate news found. Skipping...")
            return

        # Generate article using Gemini
        print("Generating AI Article...")
        article = write_article(title, description)

        # Save to WordPress Draft
        print("Creating WordPress Draft...")
        result = create_draft(title, article)

        print("===================================")
        print("Draft Created Successfully!")
        print("Post ID :", result.get("id"))
        print("Post URL:", result.get("link"))
        print("===================================")

    except Exception as e:
        print("ERROR:", str(e))


if __name__ == "__main__":
    main()
