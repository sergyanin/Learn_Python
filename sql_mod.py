import re
import sqlite3
from sqlite3 import Error
import re_mod


# def sql_connection():

#     try:
#         con = sqlite3.connect('countries.sqlite')
#         print("Connection is established: Database is created in memory")
#     except Error:
#         print(Error)
#     finally:
#         con.close()


# sql_connection()

# Выдача из трёх таблиц одновременно c использованием функции

def sql_select(word):
    return f"SELECT city.name, region.name, country.name  FROM country LEFT JOIN region ON country.country_id = region.country_id LEFT JOIN city ON region.region_id = city.region_id WHERE city.name = '{word}'"


def sql_select_country(word):
    return f"SELECT city.name, country.name  FROM country LEFT JOIN city ON country.country_id = city.country_id WHERE city.name = '{word}'"


def sql_insert(word):
    pass


def sql_search(word):
    db = sqlite3.connect('countries.sqlite')
    c = db.cursor()
    # c.execute(sql_select(word))
    c.execute(sql_select_country(word))
    found_item = c.fetchall()
    db.commit()
    db.close()
    return found_item



# print(cities)

# db = sqlite3.connect('countries.sqlite')
# c = db.cursor()
# print(sql_sel(rg))
# c.execute("SELECT country_id FROM city WHERE name= ?", (rg,))
# res = c.fetchall()
# c.execute("SELECT name FROM country WHERE country_id= ?", (res[0][0],))
# res_country = c.fetchall()
# print(res_country[0][0])


# c.execute("SELECT city.name FROM country LEFT JOIN region ON country.country_id = region.country_id LEFT JOIN city ON region.region_id = city.region_id WHERE city.name = ?", (rg,))
# res_country_1 = c.fetchall()
# print(res_country_1)
found_list = []
for city in cities:
    try:
        if sql_search(city):
            found_list.append(sql_search(city))

    except Error:
        print(Error)
    
print(found_list)


# db.commit()
# db.close()
