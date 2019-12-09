import re
from collections import namedtuple

# Выборка ссылки из сообщения
def href_search(text):
    url = re.search(r'https?://[^\"\s>]+', text).group()
    return url

def city_search(lst):
    t_list = re.findall(r'[А-ЯЁ]\w+', lst)
    return t_list

g = 'Горящие туры в Мексику: прямой перелет из Москвы в Канкун, трансфер и неделя в 5 * отеле «все включено» всего от 45 500 рублей за человека! Подробнее: https://triptodream.ru/2019/12/nedelya-v-meksike-45-000-rublej-5-vse-vklyucheno/'

prepositions = ['В', 'Без', 'До', 'Из', 'К', 'На', 'По', 'О', 'От', 'Перед',
                'При', 'Через', 'С', 'У', 'И', 'Нет', 'За', 'Над', 'Для', 'Об', 'Под', 'Про', ]

words_exception = ['Тур', 'Горящий', 'Подробнее', 'Горящие', ]

print(href_search(g))

cities = list(sorted(set(city_search(g)) - set(prepositions) - set(words_exception)))
print(cities)
