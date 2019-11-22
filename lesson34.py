from bs4 import BeautifulSoup
# import urllib.request
import requests
# import ssl

# gcontext = ssl.SSLContext()
url = 'https://vandrouki.ru/'

page = requests.get(url)
# print(page)

soup = BeautifulSoup(page.text, 'html.parser')

news = soup.find_all('div', class_="type-post")
# print(news)

results = []

for item in news:
    title = item.find('h2', class_='entry-title')#.get_text(strip=True)
    print(title)
    desc = item.find('div', class_="entry-content").get_text(strip=True)

    results.append({
        'title': title,
        'desc': desc,
    })
# print(results)
# f = open('newsVD.txt', 'w', encoding='utf-8')

# i = 1

# for item in results:
#     f.write(
#         f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\n\n**********************\n')
#     i += 1
# f.close()
