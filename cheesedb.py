import sqlite3

def db_exists(filename):
	from os.path import isfile, getsize

	if not isfile(filename):
		return False
	if getsize(filename) < 100:
		return False
	
	with open(filename, 'rb') as f:
		header = f.read(100)

	return header[:16] == 'SQLite format 3\x00'

def add_table():
	return 

def add_row():
	return 

def del_row():
	return 

if db_exists('db/database'):
	db = sqlite3.connect('db/database')

	cursor = db.cursor
else:
	db = sqlite3.connect("db/database");

	cursor = db.cursor()
	cursor.execute('''
		CREATE TABLE cheeses(id INTEGER PRIMARY KEY, name TEXT,
			country TEXT, recipes TEXT)
		''')
	cursor.execute('''
		CREATE TABLE countries(id INTEGER PRIMARY KEY, name TEXT,
			cheeses TEXT)
		''')
	cursor.execute('''
		CREATE TABLE recipes(id INTEGER PRIMARY KEY, name TEXT,
			cheese TEXT, instructions TEXT)
		''')
	db.commit();

db.close;
