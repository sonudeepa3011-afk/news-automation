from scraper.ranchiupdates import get_latest_news
from scraper.avenue_mail import get_latest_news
from gemini_ai import generate_news
from wordpress import create_draft
from duplicate import is_duplicate


def main():
    try:
        print("=" * 60)
        print("AI News Automation Started")
        print("=" * 60)

        print("Fetching latest news from Avenue Mail...")

        news_list = get_latest_news()

        if not news_list:
            print("No news found.")
            return

        print(f"\nTotal News Found: {len(news_list)}")

        for index, news in enumerate(news_list, start=1):

            print("\n" + "=" * 60)
            print(f"Processing News {index}")
            print("=" * 60)

            title = news["title"]
            content = news["content"]
            url = news["url"]

            print("Title:", title)
            print("URL:", url)

            # Duplicate Check
            print("Checking duplicate...")

            if is_duplicate(title):
                print("Duplicate article found. Skipping...")
                continue

            # Generate AI Article
            print("Generating AI article...")

            result = generate_news(
                title,
                content
            )

            # Create Draft
            print("Creating WordPress draft...")

            create_draft(
                result["title"],
                result["slug"],
                result["article"],
                result["meta_description"],
                result["comma_tags"]
            )

            print("Draft Created Successfully!")

        print("\n")
        print("=" * 60)
        print("Automation Completed Successfully")
        print("=" * 60)

    except Exception as e:
        print("\nERROR:")
        print(str(e))


if __name__ == "__main__":
    main()
