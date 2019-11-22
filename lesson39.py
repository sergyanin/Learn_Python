from parser_class import Parser
import re
import time
import Trip_news_data as tnd
from bs4 import BeautifulSoup
import requests

parser = Parser('https://vandrouki.ru/', 'newsVD.txt', tnd.data[0], False)

# url = 'https://vandrouki.ru/'
# print(parser.site['data'][0][0], parser.site['data'][0][1])
# results = []
# raw_html = requests.get(url)
# html = BeautifulSoup(raw_html.text, 'html.parser')

# news = html.find_all(parser.site['data'][0][0], parser.site['data'][0][1])
# # print(news)
# for item in news:
#     title = item.find(parser.site['data'][1][0],
#                       parser.site['data'][1][1]).get_text(strip=True)

#     results.append({
#         'title': title,
#     })
# print(results)
reads = parser.run()
news_actual = reads[::]
print(reads[0])
print(news_actual[0])
while True:

# word = 'Москва?'

# for i in reads:
#     if re.search(word, i['title']):
#         print(i)
# if len(news_actual) == 0:
#     news_actual.append(reads[0])
#     print(1, news_actual)
    # if reads[0] == news_actual[0]:
    #     print('равны')
    # else:
    #     print('Не равны')
    #     news_actual.append(reads[0])
    #     print(reads[0])
    #     print(news_actual)

    # continue
# else:
# wer = [{'title': 'Выпуск 6. 3 билета, которые админ взял бы себе, если бы у него была виза',
#        'desc': 'И снова: дешевые билеты из Прибалтики и Финляндии в Европу. От 700 рублей за билет в одну сторону, помогаем петербуржцам.Читать далее…'},]
# news_actual.insert(0, wer[0])


    if reads[0] in news_actual:

        print('Nothing')
        time.sleep(60 - time.time() % 1)
    else:
        news_actual.insert(0, reads[0])
        print('Append')
        print(news_actual[0])
        time.sleep(60 - time.time() % 1)
