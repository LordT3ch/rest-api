# rest-api
Simple rest api in python using Flask and sqlite3

You will need to download someting like ,,Advanced rest client" for testing or use test.py file that will try each command for you

Connect with localhost:5000 (port 5000 in default, can be changed in docker)
Then you can use:

localhost:5000/movies          - (GET) Get all the movies in database.

localhost:5000/movies/x        - (GET) Get the movie x from the database or print an error message if the id is not in database.

localhost:5000/movies          - (POST) Create a new movie with JSON format (no duplicate names!) for example: {  'title': 'Man in Black',
                                                                                                                  'description': 'Great movie...',
                                                                                                                  'release_year': 1997}

localhost:5000/movies/x        - (PUT) Change a movie with ID x title, description or release_year takes JSON as input (404 if movie not found, 400 if title or release year miss, beacause its needed)
