from flask import Flask, jsonify
from utils import search_film, year_to_year, by_rating, by_genre

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/movie/<title>')
def searching(title):
    movie = search_film(title)
    if not movie:
        return 'Извините, такого фильма нет в базе'
    return jsonify(movie)


@app.route('/movie/<int:year1>/to/<int:year2>')
def years(year1, year2):
    movies = year_to_year(year1, year2)
    if not movies:
        return 'Извините, по вашему запросу ничего не найдено'
    return jsonify(movies)


@app.route('/rating/<choise>')
def film_ratings(choise):
    movies = by_rating(choise)
    if not movies:
        return 'Извините, по вашему запросу ничего не найдено'
    return jsonify(movies)


@app.route('/genre/<genre>')
def get_genre(genre):
    movies = by_genre(genre)
    if not movies:
        return 'Извините, по вашему запросу ничего не найдено'
    return jsonify(movies)


if __name__ == '__main__':
    app.run()
