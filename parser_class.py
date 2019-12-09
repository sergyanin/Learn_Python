from bs4 import BeautifulSoup
import re
import requests
import Trip_news_data as tnd

# import ssl


class Parser:
    pass
    # raw_html = ''
    # # html = ''
    # results = []

    # def __init__(self, url, path, site, saving=True):
    #     self.url = url
    #     self.path = path
    #     self.saving = saving
    #     self.site = site

    # def get_html(self):
    #     self.raw_html = requests.get(self.url)
    #     self.html = BeautifulSoup(self.raw_html.text, 'html.parser')

    # def parsing(self):
        
    #     news = self.html.find_all(
    #         self.site['data'][0][0], self.site['data'][0][1])
    #     for item in news:
    #         title = item.find(
    #             self.site['data'][1][0], self.site['data'][1][1]).get_text(strip=True)
    #         desc = item.find(
    #             self.site['data'][2][0], self.site['data'][2][1]).get_text(strip=True)
    #         href = item.a.get('href')

    #         self.results.append({
    #             'title': title,
    #             'desc': desc,
    #             'href': href,
    #         })
    # def save(self):
    #     with open(self.path, 'w', encoding='utf-8') as f:
    #         i = 1
    #         for item in self.results:
    #             f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\n\n**********************\n')
    #             i += 1

    # def run(self):
    #     self.get_html()
    #     self.parsing()
    #     if self.saving == True:
    #         self.save()
    #     else:
    #         return Parser.results


class Parser_TTD:
    raw_html = ''
    desc = ''

    def __init__(self, url, site):
        self.url = url
        # self.path = path
        # self.saving = saving
        self.site = site

    def get_html(self):
        self.raw_html = requests.get(self.url)
        self.html = BeautifulSoup(self.raw_html.text, 'html.parser')

    def parsing(self):
        
        news = self.html.find(self.site['data'][0][0], self.site['data'][0][1])
        tags = news.find_all(self.site['data'][1])
        
        for tag in tags:
            tag_go = " ".join(tag.text.split())
            
            # print(self.desc)
            # tr= re.search(self.site['data'][2], tag_go)
            
            if re.search(self.site['data'][2], tag_go):
                break
            if re.search(r': —', tag_go):
                tag_go = tag_go.replace('; —', '\n—')
                tag_go = tag_go.replace(': —', ':\n—')
            Parser_TTD.desc = Parser_TTD.desc + tag_go + '\n'
        # print(self.desc)
        # return self.desc



    def run(self):
        self.get_html()
        self.parsing()
        return Parser_TTD.desc
