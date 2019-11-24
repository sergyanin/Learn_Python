import re
import sqlite3

prepositions = ['В', 'Без', 'До', 'Из', 'К', 'На', 'По', 'О', 'От', 'Перед',
                'При', 'Через', 'С', 'У', 'И', 'Нет', 'За', 'Над', 'Для', 'Об', 'Под', 'Про']

w = 'Иркутск, доброе утро! Для вас тут нашлись недорогие билетики на Бали - 27500 рублей за полет туда-обратно! По пути - безвизовые Пекин и Куала-Лумпур.'

t_list = re.findall(r'[А-ЯЁ]\w+', w)
t_list = list(set(t_list) - set(prepositions))
print(t_list)

db = sqlite3.connect('countries.sqlite')
c = db.cursor()
rg = 'Иркутск'

c.execute(f"SELECT country_id FROM city WHERE name = ?",(rg,))
res = c.fetchall()

print(res)









db.commit()
db.close()
