from scraper.avenue_mail import get_latest_news
from gemini_ai import generate_news
from wordpress import create_draft
from duplicate import is_duplicate


def main():
    try:
        print("Fetching latest news...")

        news_list = get_latest_news()

        if not news_list:
            print("No news found.")
            return

        print(f"Found {len(news_list)} news articles.")

        for news in news_list:

            title = news["title"]
            description = news.get("description", "")

            print(f"\nChecking: {title}")

            # Duplicate Check
            if is_duplicate(title):
                print("Duplicate Found. Skipping...")
                continue

            print("Generating AI Article...")

            result = generate_news(
                title,
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

            print("Draft Created Successfully.\n")

        print("====================================")
        print("Automation Completed Successfully ✅")
        print("====================================")

    except Exception as e:
        print("ERROR:", str(e))


if __name__ == "__main__":
    main()
