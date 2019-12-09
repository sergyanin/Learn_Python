from parser_class import Parser, Parser_TTD
import re
import time
import Trip_news_data as tnd
from bs4 import BeautifulSoup
import requests
# import short_url
# from resorts import resorts


# parser = Parser('https://vandrouki.tours/default-city/budet-krasivo-3-7-nochej-v-iordanii-ot-12100-s-cheloveka-kucha-dat-ves-dekabr-bez-viz/',
                # 'newsVTours.txt', tnd.data[0], False)

# url = 'https://vandrouki.tours/default-city/hajnan-letim-na-10-nochej-v-seredine-dekabrya-za-24600-s-cheloveka-iz-moskvy-bez-viz/'


# raw_html = requests.get(url)
# soup = BeautifulSoup(raw_html.text, 'html.parser')
# # print(html)

# results = []

# news = soup.find('div', {'class': 'tt-content'})
# # print(news)
# # for item in news:
# #     desc = item.find('p', 'li').get_text(strip=True)
# #     results.append(desc)
# # print(results)
# tags = news.find_all(['p', 'li'])
# desc = ''
# for tag in tags:
#     tag_go = " ".join(tag.text.split())
#     if re.search('Этеншн', tag_go):
#         break
#     # elif re.search(r'Когда летим', tag_go):
#     tag_go = re.sub(r'Когда летим\?', 'Когда:', tag_go)
#     tag_go = re.sub(r'Виза\?', 'Виза:', tag_go)

#     desc = desc + '\n' + tag_go

# print(desc)


url = 'https://triptodream.ru/2019/12/nedelya-v-goa-13-800-rublej/'


# raw_html = requests.get(url)
# soup = BeautifulSoup(raw_html.text, 'html.parser')
# news = soup.find(tnd.data[2]['data'][0][0], tnd.data[2]['data'][0][1])
# tags = news.find_all(tnd.data[2]['data'][1])
# desc = ''
# for tag in tags:
#     tag_go = " ".join(tag.text.split())
#     if re.search(tnd.data[2]['data'][2], tag_go):
#         break
#     if re.search(r'; —', tag_go):
#         tag_go = tag_go.replace('; —', '\n—')
#         tag_go = tag_go.replace(': —', ':\n—')

    # print(tag_go)
    # tag_go = re.sub(r'Виза\?', 'Виза:', tag_go)

    # desc = desc + tag_go + '\n'

# print(desc)

parser = Parser_TTD(url, tnd.data[2])
text_news = parser.run()
print(text_news)
