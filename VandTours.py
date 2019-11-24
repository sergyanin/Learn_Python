from parser_class import Parser
import re
import time
import Trip_news_data as tnd
from bs4 import BeautifulSoup
import requests
import short_url
from resorts import resorts


parser = Parser('https://vandrouki.tours/default-city/budet-krasivo-3-7-nochej-v-iordanii-ot-12100-s-cheloveka-kucha-dat-ves-dekabr-bez-viz/',
                'newsVTours.txt', tnd.data[0], False)

url = 'https://vandrouki.tours/default-city/hajnan-letim-na-10-nochej-v-seredine-dekabrya-za-24600-s-cheloveka-iz-moskvy-bez-viz/'


raw_html = requests.get(url)
soup = BeautifulSoup(raw_html.text, 'html.parser')
# print(html)

results = []

news = soup.find('div', {'class': 'tt-content'})
# print(news)
# for item in news:
#     desc = item.find('p', 'li').get_text(strip=True)
#     results.append(desc)
# print(results)
tags = news.find_all(['p', 'li'])
desc = ''
for tag in tags:
    tag_go = " ".join(tag.text.split())
    if re.search('Этеншн', tag_go):
        break
    # elif re.search(r'Когда летим', tag_go):
    tag_go = re.sub(r'Когда летим\?', 'Когда:', tag_go)
    tag_go = re.sub(r'Виза\?', 'Виза:', tag_go)

    desc = desc + '\n' + tag_go

print(desc)
