import sqlite3 as sql
from collections import namedtuple


# natively supported SQLite  types
T = "TEXT"
I = "INTEGER"
F = "FLOAT"
R = 'REAL'
B = 'BLOB'
N = 'NULL'


class Database:

	def __init__(self, dbfile, **kwargs):
		# Start a connection to the database
		self.connection = sql.connect(dbfile, **kwargs)
		self.cursor = self.connection.cursor()

	def revert(self):
		self.connection.rollback()


Quote = namedtuple('Quote', 'id, author, quote')


class QuotesDB(Database):
	def __init__(self, file):
		super().__init__(file, check_same_thread=False)

	def add_quote(self, **params):
		with self.connection:
			self.cursor.execute(
				"INSERT INTO quotes (id, author, quote) VALUES (?, ?, ?)",
				(params['id'], params['author'], params['quote'])
			)

	def delete_quote(self, id_):
		try:
			with self.connection:
				self.cursor.execute(
					"DELETE FROM quotes WHERE id=?",
					(id_, )
				)
			return True
		except sql.IntegrityError as error:
			print(error)
			return False

	def exists(self, id_):
		with self.connection:
			self.cursor.execute(
				"SELECT author FROM quotes WHERE id=?",
				(id_)
			)
			return bool(self.fetchone())

	def update_quote(self, id_, **params):
		pass

	def get_all_quotes(self, by=None):
		with self.connection:
			if by:
				self.cursor.execute(
					"SELECT id, author, quote FROM quotes WHERE author=?",
					(by, )
				)
			else:
				self.cursor.execute(
					"SELECT id, author, quote FROM quotes",
				)
			return map(Quote._make, self.cursor.fetchall())
