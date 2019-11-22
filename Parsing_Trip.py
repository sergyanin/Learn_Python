from parser_class import Parser
import re
import time
import Trip_news_data as tnd
from bs4 import BeautifulSoup
import requests

parser1 = Parser('https://triptodream.ru/', 'newsTtD.txt', tnd.data[1], False)

reads1 = parser1.run()
news_actual = reads1[::]
print(reads1[0])
print(news_actual[0])
