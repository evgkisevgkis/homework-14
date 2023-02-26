import sqlite3


def search_film(title_entered):
    """Функция для поиска фильма в базе"""
    query = f"SELECT title, country, release_year, listed_in, description FROM netflix WHERE title = '{title_entered}' ORDER BY date_added DESC"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def year_to_year(year1, year2):
    """Функция для поиска фильмов, вышедших между годами"""
    query = f"SELECT title, release_year FROM netflix WHERE release_year BETWEEN {year1} AND {year2} LIMIT 100"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    return result


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
        return result
    elif choise == 'family':
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query2)
            result = cursor.fetchall()
        return result
    elif choise == 'adult':
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query3)
            result = cursor.fetchall()
        return result


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
    query = f"SELECT title, 'cast' from netflix WHERE 'cast' LIKE '%{actor1}%' OR 'cast' LIKE '%{actor2}%'"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def advanced_search(ftype, year, genre):
    """Данная фунцкия позволяет использовать поиск по 3 критериям"""
    query = f"SELECT title, description FROM netflix WHERE netflix.type = {ftype} AND release_year = {year} AND listed_in LIKE '%{genre}%'"

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    return result


#advanced_search('Movie', 2022, 'Dramas')
