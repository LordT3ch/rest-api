import requests
import os
import json

BASEURL = "http://127.0.0.1:5000/"

#CLEAR CONSOLE
os.system('cls')

#GET ALL MOVIES
response = requests.get(BASEURL + "movies")
print('v GET ALL MOVIES v', '\n', response.json(), '\n')
input()

#GET MOVIE WITH ID 44 (SHOULD RETURN AN ERROR 404)
response = requests.get(BASEURL + "movies/44")
print('v GET ID 4 v', '\n', response.json(), '\n')
input()

#GET MOVIE WITH ID 1
response = requests.get(BASEURL + "movies/1")
print('v GET ID 1 v', '\n', response.json(), '\n')
input()


#POST MOVIE (NO DUPLICATE NAMES)
movie = {  'title': 'Man in Black',
            'description': 'Great movie...',
            'release_year': 1997
}

response = requests.post(BASEURL + "movies", data=json.dumps(movie))
print('v POST MOVIE (ONLY RESPONSE 201 OR 409 IF MOVIE ALREADY EXISTS) v', '\n', response, '\n')
input()

#PUT MOVIE WITH ID 1
movie = {  'title': 'Matrix Test',
            'description': 'The Matrix is a computer-generated gream world...',
            'release_year': 2033
}

response = requests.put(BASEURL + "movies/1", data=json.dumps(movie))
print('v PUT MOVIE IN ID 1 CHANGED TITLE AND RELEASE YEAR v', '\n', response.json(), '\n')
input()

#PUT MOVIE WITH ID 1
movie = {  'title': 'The Matrix',
            'description': 'The Matrix is a computer-generated gream world...',
            'release_year': 1999
}

response = requests.put(BASEURL + "movies/1", data=json.dumps(movie))
print('v PUT MOVIE IN ID 1 CHANGED TITLE AND RELEASE YEAR BACK v', '\n', response.json(), '\n')