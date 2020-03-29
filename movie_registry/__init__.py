import markdown
import os
import shelve

from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    if 'db' not in g:
        g.db = shelve.open("movies.db")
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@app.route('/')

class MovieList(Resource):	
	def get(self):
		shelf = get_db()
		keys  = list(shelf.keys())
		
		movies = []

		for key in keys:
			movies.append(shelf[key])

		return {'message': 'Success', 'data': movies}, 200

	def post(self):
		shelf  = get_db()		
		parser = reqparse.RequestParser()

		parser.add_argument('identifier', required=True)
		parser.add_argument('name', required=True)
		parser.add_argument('movie_type', required=True)
		parser.add_argument('movie_year', required=True)

		arguments = parser.parse_args()
		shelf[arguments['identifier']] = arguments

		return {'message': 'Movie save with success', 'data': arguments}, 201

class Movie(Resource):
	def get(self, identifier):
		shelf = get_db()

		if not (identifier in shelf):
			return {'message': 'Movie not found', 'data': {}}, 404

		return {'message': 'Movie found', 'data':shelf[identifier]}, 200	
	def put(self, identifier):
		shelf = get_db()
		update_fields = shelf[identifier]
		parser = reqparse.RequestParser()

		if not (identifier in shelf):
			return {'message': 'Movie not found', 'data': {}}, 404

		parser.add_argument('name', type=str)
		parser.add_argument('movie_type', type=str)
		parser.add_argument('movie_year', type=int)

		arguments = parser.parse_args()
		update_fields['name'] = arguments.get('name', None)
		update_fields['movie_type'] = arguments.get('movie_type', None)
		update_fields['movie_year'] = arguments.get('movie_year', None)
		shelf[identifier] = update_fields

		return {'message': 'Movie found', 'data':shelf[identifier]}, 200

	def delete(self, identifier):
		shelf = get_db()

		if not (identifier in shelf):
			return {'message': 'Movie not found', 'data': {}}, 404

		del shelf[identifier]	
		return '', 204	

api.add_resource(MovieList, '/movies')
api.add_resource(Movie, '/movies/<string:identifier>')