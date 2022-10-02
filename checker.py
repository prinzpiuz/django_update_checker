"""
script to check if there any django updates/bugfixes/security fixes released,
from the website https://www.djangoproject.com/weblog/
"""
from datetime import datetime, timedelta
import argparse
import feedparser

from teams import send_teams_msg

DEFAULT_KEY_WORDS_TO_TRACK = ["releases", "released", "release", "bugfix"]

# to give 1 day delay to manage the time updates are publishing
def main():
    """main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="incoming ms teams webhook url", type=str)
    parser.add_argument(
        "--words", help="pattern to match in title string", type=str, required=False
    )
    args = parser.parse_args()
    date = datetime.today() - timedelta(days=1)
    month = date.month
    day = date.day
    year = date.year
    if args.url:
        if args.words:
            DEFAULT_KEY_WORDS_TO_TRACK.extend(args.words.split(","))
        print(f"words currently tracking {DEFAULT_KEY_WORDS_TO_TRACK}")
        parsed_data = feedparser.parse("https://www.djangoproject.com/rss/weblog/")
        if parsed_data.status == 200:
            for item in parsed_data.entries:
                link = item.link
                title = item.title
                summary = item.summary
                pub_year = item.published_parsed.tm_year
                pub_month = item.published_parsed.tm_mon
                pub_date = item.published_parsed.tm_mday
                if (
                    day == pub_date
                    and month == pub_month
                    and year == pub_year
                    and any(word in title for word in DEFAULT_KEY_WORDS_TO_TRACK)
                ):
                    print(title)
                    send_teams_msg(args.url, title, link, summary)
        else:
            print("website not available")
    else:
        print("webhook url not passed")


if __name__ == "__main__":
    main()
