from scraper.ranchiupdates import get_latest_news as ranchi_news
from scraper.avenue_mail import get_latest_news as avenue_news

from gemini_ai import generate_news
from wordpress import create_draft
from duplicate import is_duplicate


def main():

    print("=" * 60)
    print("AI News Automation Started")
    print("=" * 60)

    news_list = []

    print("Fetching RanchiUpdates News...")
    try:
        news_list.extend(ranchi_news())
        print(f"RanchiUpdates: {len(news_list)} News")
    except Exception as e:
        print("RanchiUpdates Error:", e)

    print("Fetching Avenue Mail News...")
    try:
        avenue = avenue_news()
        news_list.extend(avenue)
        print(f"Avenue Mail: {len(avenue)} News")
    except Exception as e:
        print("Avenue Mail Error:", e)

    if not news_list:
        print("No News Found.")
        return

    print(f"\nTotal News Collected: {len(news_list)}")

    processed = 0

    for index, news in enumerate(news_list, start=1):

        try:

            print("\n" + "=" * 60)
            print(f"Processing News {index}")
            print("=" * 60)

            title = news.get("title", "")
            content = news.get("content", "")
            url = news.get("url", "")

            print("Title :", title)
            print("URL   :", url)

            if is_duplicate(title):
                print("Duplicate Found. Skipping...")
                continue

            print("Generating AI Article...")

            result = generate_news(title, content)

            print("Creating WordPress Draft...")

            create_draft(
                result["title"],
                result["slug"],
                result["article"],
                result["meta_description"],
                result["comma_tags"]
            )

            processed += 1

            print("Draft Created Successfully!")

        except Exception as e:
            print("Error:", e)
            continue

    print("\n" + "=" * 60)
    print("Automation Completed")
    print(f"Total Draft Created : {processed}")
    print("=" * 60)


if __name__ == "__main__":
    main()
