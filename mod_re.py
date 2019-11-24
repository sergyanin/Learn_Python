import re
import sqlite3

prepositions = ['В', 'Без', 'До', 'Из', 'К', 'На', 'По', 'О', 'От', 'Перед',
                'При', 'Через', 'С', 'У', 'И', 'Нет', 'За', 'Над', 'Для', 'Об', 'Под', 'Про']

w = 'Иркутск, доброе утро! Для вас тут нашлись недорогие билетики на Бали - 27500 рублей за полет туда-обратно! По пути - безвизовые Пекин и Куала-Лумпур.'

t_list = re.findall(r'[А-ЯЁ]\w+', w)
t_list = list(set(t_list) - set(prepositions))
# print(t_list)

db = sqlite3.connect('countries.sqlite')
c = db.cursor()
rg = 'Пекин'

# c.execute("SELECT country_id FROM city WHERE name= ?", (rg,))
# res = c.fetchall()
# c.execute("SELECT name FROM country WHERE country_id= ?", (res[0][0],))
# res_country = c.fetchall()
# print(res_country[0][0])

c.execute("SELECT city.name, country.name  FROM country LEFT JOIN city ON country.country_id = city.country_id WHERE city.name = ?", (rg,))
res_country_1 = c.fetchall()
print(res_country_1)
db.commit()
db.close()
