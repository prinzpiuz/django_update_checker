"""
script to check if there any django updates/bugfixes/security fixes released,
from the website https://www.djangoproject.com/weblog/
"""
import requests as r
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pymsteams
import argparse

# to give 1 day delay to manage the time updates are publishing
date = datetime.today() - timedelta(days=1)
month = date.strftime("%b").lower()
day = date.strftime("%d")
year = date.strftime("%Y")
parser = argparse.ArgumentParser()
parser.add_argument('--url', help='incoming ms teams webhook url')
args = parser.parse_args()
if args.url:
    html = r.get("https://www.djangoproject.com/weblog/")
    if html.status_code is 200:
        soup = BeautifulSoup(html.content, 'html.parser')
        for item in soup.find(attrs={"class": "list-news"}).find_all('li'):
            a_tag = item.find('a')
            title = a_tag.get_text()
            splitted_url = a_tag.get('href').split('/')
            pub_year = splitted_url[4]
            pub_month = splitted_url[5]
            pub_date = splitted_url[6]
            avatar_url = "https://avatars.githubusercontent.com/u/27804?s=200&v=4"
            if day == pub_date and month == pub_month and year == pub_year:
                try:
                    teams_message = pymsteams.connectorcard(args.url)
                    teams_message.text("Django Update Available")
                    teams_message.color("#0C4B33")
                    teams_message_card = pymsteams.cardsection()
                    teams_message_card.activityImage(avatar_url)
                    teams_message_card.activityTitle(title)
                    teams_message_card.activitySubtitle(
                        '<a href="{}">Read More Here</a>'.format(a_tag.get('href')))
                    teams_message.addSection(teams_message_card)
                    teams_message.send()
                except pymsteams.TeamsWebhookException as e:
                    print(e)
    else:
        print("website not available")
else:
    print("webhook url not passed")
