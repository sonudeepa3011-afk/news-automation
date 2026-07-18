from newsdata import get_latest_news
from gemini_ai import generate_news
from wordpress import create_draft
from duplicate import is_duplicate
from scraper.avenue_mail import get_latest_news

def main():
    try:
        print("Fetching latest news...")

        news = get_latest_news()

        if not news:
            print("No news found.")
            return

        original_title = news.get("title", "")
        description = news.get("description", "")

        # Duplicate Check
        if is_duplicate(original_title):
            print("Duplicate news found. Skipping...")
            return

        print("Generating AI Article...")

        result = generate_news(
            original_title,
            description
        )

        print("Creating WordPress Draft...")

        create_draft(
            result["title"],
            result["slug"],
            result["article"],
            result["meta_description"],
            result["comma_tags"]
        )

        print("======================================")
        print("Automation Completed Successfully ✅")
        print("======================================")

    except Exception as e:
        print("ERROR:", str(e))


if __name__ == "__main__":
    main()
