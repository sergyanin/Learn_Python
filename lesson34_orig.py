from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://vandrouki.ru/')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup)
# news = soup.find_all('div', class_="type-post")

# results = []

# for item in news:
#     title = item.find('h2', class_='entry-title').get_text(strip=True)
#     desc = item.find('div', class_="entry-content").get_text(strip=True)
#     results.append({
#         'title': title,
#         'desc': desc,
#     })

# f = open('news1.txt', 'w', encoding='utf-8')
# i = 1
# for item in results:
#     f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\n\n**********************\n')
#     i += 1
# f.close()
