from newsdata import get_latest_news

def main():
    try:
        news = get_latest_news()

        print("=" * 50)
        print("LATEST NEWS")
        print("=" * 50)

        print("Title :", news.get("title"))
        print("Source:", news.get("source_name"))
        print("Date  :", news.get("pubDate"))
        print("Link  :", news.get("link"))

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()
