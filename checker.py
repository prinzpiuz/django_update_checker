"""
script to check if there any django updates/bugfixes/security fixes released,
from the website https://www.djangoproject.com/weblog/
"""
import requests as r
from bs4 import BeautifulSoup
import datetime

date = datetime.datetime.today()
month = date.strftime("%b").lower()
day = date.strftime("%d")
year = date.strftime("%Y")
html = r.get("https://www.djangoproject.com/weblog/")
if html.status_code is 200:
    soup = BeautifulSoup(html.content, 'html.parser')
    for item in soup.find(attrs={"class": "list-news"}).find_all('li'):
        a_tag = item.find('a')
        splitted_url = a_tag.get('href').split('/')
        pub_year = splitted_url[4]
        pub_month = splitted_url[5]
        pub_date = splitted_url[6]
        # print(year, month, day)
        # print(pub_year, pub_month, pub_date)
    print(a_tag.get_text())
else:
    print("website not availabel")
