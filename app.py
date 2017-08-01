import sqlite3
from flask import Flask, request, jsonify

import json

app = Flask(__name__)


@app.route('/api/places', methods=['GET', 'POST'])
def collection():
	if request.method == 'GET':
		all_places = get_all_places()
		return json.dumps(all_places)
	elif request.method == 'POST':
		data = request.form
		result = add_place(data['name'], data['country'], data['rating'])
		return jsonify(result)


@app.route('/api/places/<place_id>', methods=['GET'])
def resource(place_id):
	if request.method == 'GET':
		place = get_place(place_id)
		return json.dumps(place)
	else:
		return 'error'


def add_place(name, country, rating):
	try:
		with sqlite3.connect('places.db') as connection:
			cursor = connection.cursor()
			cursor.execute("""INSERT INTO places (name, country, rating) VALUES (?, ?, ?);""", (name, country, rating))
			result = {'status': 1, 'message': 'Place added'}
	finally:
		result = {'status': 0, 'message': 'error'}
	return result


def get_place(place_id):
	with sqlite3.connect('places.db') as connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM places WHERE place_id = ?", place_id)
		place = cursor.fetchone()
		return place


def get_all_places():
	with sqlite3.connect('places.db') as connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM places ORDER BY id DESC")
		all_places = cursor.fetchall()
		return all_places


def get_single_place(place_id):
	with sqlite3.connect('places.db') as connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM places WHERE id = ?", place_id)
		song = cursor.fetchone()
		return song


if __name__ == '__main__':
	app.debug = True
	app.run()
