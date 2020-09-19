"""Representational state transfer (REST) API using Flask ."""

from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import json


QUOTES = []
with open('quotes.json') as file:
	QUOTES = json.load(file)


class Quote(Resource):
	"""Quotes interface."""

	def _get_params_(self, *reqs):
		parser = reqparse.RequestParser()
		for req in reqs:
			parser.add_arguments(req)
		return parser.parse_args()

	def delete(self, id_):
		"""Delete an existing quote with the specified id."""
		global QUOTES
		QUOTES = [*filter(
			lambda quote: quote['id'] != id_,
			QUOTES
		)]
		return f'Quote with id {id_} has been successfully deleted.', 200

	def get(self, id_=0):
		"""
		Retrieve a random quote or a quote with a specified id other than 0.
		"""
		if not id_:
			return random.choice(QUOTES)

		if id_ == 'all':
			return QUOTES

		for quote in QUOTES:
			if quote['id'] == id_:
				return quote, 200

		return 'Quote not found', 404


	def post(self, id_):
		"""Adds/creates a new quote."""

		for quote in QUOTES:
			if quote['id'] == id_:
				return f"Quote with id {id_} already exists", 400

		params = self._get_params_('author', 'quote')
		quote = {
			"id": int(id_),
			"author": params["author"],
			"quote": params["quote"]
		}

		QUOTES.append(quote)
		return quote, 201

	def put(self, id_):
		"""Add or modify an existing quote with the specified id."""

		params = self._get_params_('author', 'quote')
		for quote in QUOTES:
			if quote['id'] == id_:
				quote['author'] = params['author']
				quote['quote'] = params['quote']
				return quote, 200

		quote = {
			'id': id_,
			'author': params['author'],
			'quote': params['quote']
		}
		QUOTES.append(quote)
		return quote, 201


# setup application
app = Flask(__name__)
api = Api(app)

# add resource to api
api.add_resource(
	Quote,
	# resource urls
	'/some-quotes',
	'/some-quotes/',
	'/some-quotes/<int:id_>',
	'/some-quotes/<string:id_>'
)


if __name__ == '__main__':
	app.run(debug=True)
