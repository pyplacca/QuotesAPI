"""Representational state transfer (REST) API using Flask ."""

from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import json
import db


class PopularQuotes(Resource):
	"""Quotes interface."""

	def _get_params_(self, *reqs):
		parser = reqparse.RequestParser()
		for req in reqs:
			parser.add_argument(req)
		return parser.parse_args()

	def delete(self, id_):
		"""Delete an existing quote with the specified id."""
		res = qdb.delete_quote(id_)
		if res:
			return f'Quote with id {id_} has been successfully deleted.', 200
		else:
			return f'Quote with id {id_} does not exist!', 404

	def get(self, id_=0):
		"""
		Retrieve a random quote or a quote with a specified id other than 0.
		"""
		quotes = qdb.get_all_quotes()

		if isinstance(id_, str):
			if id_ == 'all':
				return self.get_all()
			return self.get_by_name(id_)

		if not id_:
			return dict(random.choice([*quotes])._asdict())

		for quote in quotes:
			if quote.id == id_:
				return dict(quote._asdict()), 200

		del quotes
		return 'Quote not found', 404

	def get_by_name(self, name):
		quotes = [*qdb.get_all_quotes(by=name)]
		if quotes:
			return [*map(lambda quote: dict(quote._asdict()), quotes)], 200
		return 'Author not found', 404

	def get_all(self):
		return [*map(
			lambda quote: dict(quote._asdict()),
			quotes
		)], 200

	def post(self, id_):
		"""Adds/creates a new quote."""

		if qdb.exists(id_):
			return f"Quote with id {id_} already exists", 400

		params = self._get_params_('author', 'quote')
		qdb.add_quote(
			id=int(id_),
			author=params['author'],
			quote=params['quote']
		)
		return quote, 201

	def put(self, id_):
		"""Modify existing quote with specified id."""

		params = self._get_params_('author', 'quote')
		try:
			with database.connection:
				database.connection.execute(
					"UPDATE quotes SET author=?, quote=? WHERE id=?",
					(params['author'], params['quote'], id_)
				)
			return quote, 200
		except (db.sql.OperationalError, db.sql.IntegrityError) as error:
			print(error)
			self.post(id_)
			return quote, 201


# connect to quotes database
qdb = db.QuotesDB('database.db')


# setup application
app = Flask(__name__)
api = Api(app)

# add resource to api
api.add_resource(
	PopularQuotes,
	# resource urls
	'/popular-quotes',
	'/popular-quotes/',
	'/popular-quotes/<int:id_>',
	'/popular-quotes/<string:id_>'
)


if __name__ == '__main__':
	try:
		app.run(debug=True)
	except KeyboardInterrupt:
		print('Server closed!')
