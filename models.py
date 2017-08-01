import sqlite3

from flask import Flask


app = Flask(__name__)


def drop_table():
	with sqlite3.connect('places.db') as connection:
		c = connection.cursor()
		c.execute("""DROP TABLE IF EXISTS places;""")
	return True


def create_db():
	with sqlite3.connect('places.db') as connection:
		c = connection.cursor()
		table = """CREATE TABLE places(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL,
			country TEXT NOT NULL,
			rating INTEGER NOT NULL 
		);
			"""
		c.execute(table)
	return True

if __name__ == '__main__':
	drop_table()
	create_db()
