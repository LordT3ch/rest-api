import json
from flask import Flask, request
from flask_restful import Resource, Api
import sqlite3

conn = sqlite3.connect('movies.sqlite', check_same_thread=False)
cur = conn.cursor()

#Use once to create database items
cur.execute('''CREATE TABLE IF NOT EXISTS movies( id integer PRIMARY KEY AUTOINCREMENT, title text UNIQUE, description text, release_year int)''')
cur.execute('''INSERT OR REPLACE INTO movies VALUES(1,'The Matrix','The Matrix is a computer-generated gream world...',1999)''')
cur.execute('''INSERT OR REPLACE INTO movies VALUES(2,'The Matrix Reloaded','Continuation of the cult classic The Matrix...',2003)''')
conn.commit()
#

app = Flask(__name__)
api = Api(app)

col_names = ["id", "title", "description", "release_year"]

@app.route('/movies')
def getMoviesList():

    mov_list=[]
    cur.execute("SELECT * FROM movies")
    data = cur.fetchall()

    for row in data:
        row_dict={}

        for i in range(len(col_names)):
            row_dict[col_names[i]] = row[i]
        mov_list.append(row_dict)

    return json.dumps(mov_list)
    
@app.route('/movies/<int:id>')
def getMovieById(id):

    conn = sqlite3.connect('movies.sqlite', check_same_thread=False)
    cur = conn.cursor()

    sql = "SELECT * FROM movies WHERE id = ?"

    cur.execute(sql, (id,))
    movie = cur.fetchone()

    if movie is None:
        error_message = {'error': 'ID not found'}
        return json.dumps(error_message), 404

    mov_dict={}
    for i in range(len(col_names)):
        mov_dict[col_names[i]] = movie[i]

    return json.dumps(mov_dict)

@app.route('/movies', methods=['POST'])
def postMovie():
    data = request.get_json(force=True)
    title = data.get('title')
    release_year = data.get('release_year')
    description = data.get('description')

    if not title or not release_year:
        error_message = {'error': 'title and release_year are required.'}
        return json.dumps(error_message), 400
    

    try:
        sql = "INSERT INTO movies (title, description, release_year) VALUES (?, ?, ?)"

        cur.execute(sql, (title, description, release_year,))
        conn.commit()
    except sqlite3.IntegrityError:
        error_message = {'error': 'Movie with this name already exists'}
        return json.dumps(error_message), 409
    return '',201
        
@app.route('/movies/<int:id>', methods=['PUT'])
def putMovie(id):

    data = request.get_json(force=True)
    title = data.get('title')
    release_year = data.get('release_year')
    description = data.get('description')

    if not title or not release_year:
        error_message = {'error': 'title and release_year are required.'}
        return json.dumps(error_message), 400
    
    cur.execute("SELECT * FROM movies WHERE id = ?", (id,))
    movie = cur.fetchone()

    if movie is None:
        error_message = {'error': 'Movie not found.'}
        return json.dumps(error_message), 404
    
    sql = "UPDATE movies SET title = ?, release_year = ?, description = ? WHERE id = ?"
    cur.execute(sql, (title, release_year, description, id))
    conn.commit()

    cur.execute("SELECT * FROM movies WHERE id = ?", (id,))
    updated_movie = cur.fetchone()

    response = {
            'id': updated_movie[0],
            'title': updated_movie[1],
            'release_year': updated_movie[2],
            'description': updated_movie[3]
        }
    json_response = json.dumps(response)
    return json_response, 200


if __name__ == '__main__':
    app.run()





# 1. GET MOVIES LIST /movies #* ✓
# 2. GET MOVIE BY ID /movies/<int:id> #* ✓
# 3. POST /movies create a movie in database with JSON format #* ✓
# 4. PUT /movies/<int:id> update a movie with specified id, should accept JSON format #* ✓