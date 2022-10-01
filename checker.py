"""
script to check if there any django updates/bugfixes/security fixes released,
from the website https://www.djangoproject.com/weblog/
"""
from datetime import datetime, timedelta
import argparse
from typing import List
import feedparser
import pymsteams


def send_teams_msg(teams_url: str, card_title: str, card_link: str):
    """To generate and send message in teans

    Args:
        title (str): tittle for the card
        link (str): link in the card
    """
    try:
        avatar_url = "https://avatars.githubusercontent.com/u/27804?s=200&v=4"
        teams_message = pymsteams.connectorcard(teams_url)
        teams_message.text("Django Update Available")
        teams_message.color("#0C4B33")
        teams_message_card = pymsteams.cardsection()
        teams_message_card.activityImage(avatar_url)
        teams_message_card.activityTitle(card_title)
        teams_message_card.activitySubtitle(f'<a href="{card_link}">Read More Here</a>')
        teams_message.addSection(teams_message_card)
        teams_message.send()
    except pymsteams.TeamsWebhookException as error:
        print(error)


# to give 1 day delay to manage the time updates are publishing
date = datetime.today() - timedelta(days=1)
default_world_to_track = ["releases", "released", "release", "bugfix"]
month = date.month
day = date.day
year = date.year
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="incoming ms teams webhook url", type=str)
parser.add_argument(
    "--words",
    help="pattern to match in title string",
    type=List,
    default=default_world_to_track,
)
args = parser.parse_args()
if args.url:
    if args.words:
        default_world_to_track.extend(args.words)
    print(f"words currently tracking {default_world_to_track}")
    parsed_data = feedparser.parse("https://www.djangoproject.com/rss/weblog/")
    if parsed_data.status == 200:
        for item in parsed_data.entries:
            link = item.link
            title = item.title
            pub_year = item.published_parsed.tm_year
            pub_month = item.published_parsed.tm_mon
            pub_date = item.published_parsed.tm_mday
            if (
                day == pub_date
                and month == pub_month
                and year == pub_year
                and any(word in title for word in default_world_to_track)
            ):
                print(title)
                send_teams_msg(args.url, title, link)
    else:
        print("website not available")
else:
    print("webhook url not passed")
