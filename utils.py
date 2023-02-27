import sqlite3
import json


def search_film(title_entered):
    """Функция для поиска фильма в базе"""
    query = f"SELECT title, country, release_year, listed_in, description FROM netflix WHERE title = '{title_entered}' ORDER BY date_added DESC"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    total = []
    for elem in result:
        total.append({
            "title": elem[0],
            "country": elem[1],
            "release_year": elem[2],
            "genre": elem[3],
            "description": elem[4]
        })
    return total


def year_to_year(year1, year2):
    """Функция для поиска фильмов, вышедших между годами"""
    query = f"SELECT title, release_year FROM netflix WHERE release_year BETWEEN {year1} AND {year2} LIMIT 100"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    total = []
    for elem in result:
        total.append({
            "title": elem[0],
            "release_year": elem[1]
        })
    return total


def by_rating(choise):
    """Функция для выдачи фильмов по рейтингу"""
    query1 = f"SELECT title, rating, description FROM netflix WHERE rating = 'G'"
    query2 = f"SELECT title, rating, description FROM netflix WHERE rating = 'G' OR rating = 'PG' OR rating ='PG-13'"
    query3 = f"SELECT title, rating, description FROM netflix WHERE rating = 'R' OR rating = 'NC-17'"

    if choise == 'children':
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query1)
            result = cursor.fetchall()

    elif choise == 'family':
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query2)
            result = cursor.fetchall()

    elif choise == 'adult':
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query3)
            result = cursor.fetchall()
    total = []
    for elem in result:
        total.append({
            "title": elem[0],
            "rating": elem[1],
            "description": elem[2]
        })
    return total


def by_genre(genre):
    """Данная фунуция возвращает 10 самых новых фильмов по данному жанру"""
    query = f"SELECT title, description FROM netflix WHERE listed_in LIKE '%{genre}%' ORDER BY release_year DESC LIMIT 10"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def find_actors(actor1, actor2):
    """Функция получает имена двух актеров и возвращает тех, с кем они играли более двух раз"""
    query = f"SELECT netflix.cast from netflix WHERE netflix.cast LIKE '%{actor1}%' AND netflix.cast LIKE '%{actor2}%'"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    for i in result:
        if i.count > 2:
            print(i)


def advanced_search(ftype, year, genre):
    """Данная фунцкия позволяет использовать поиск по 3 критериям"""
    query = f"SELECT title, description FROM netflix WHERE netflix.type = '{ftype}' AND release_year = {year} AND listed_in LIKE '%{genre}%'"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    return json.dumps(result)


# print(find_actors('Rose McIver', 'Ben Lamb'))
# print(advanced_search('Movie', 2011, 'Dramas'))
