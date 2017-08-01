import sqlite3


def drop_table():
	with sqlite3.connect('places.db') as conn:
		c = conn.cursor()
		c.execute("""DROP TABLE IF EXISTS places;""")
	return True


def create_db():
	with sqlite3.connect('places.db') as conn:
		c = conn.cursor()
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
