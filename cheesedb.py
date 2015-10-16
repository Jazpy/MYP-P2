import sqlite3
import table_objects

def create_db(db):
	cursor = db.cursor()
	cursor.execute('CREATE TABLE cheeses(name TEXT, softness TEXT)')
	cursor.execute('CREATE TABLE countries(name TEXT)')
	cursor.execute('''CREATE TABLE recipes(name TEXT, instructions TEXT,
		time TEXT)''')
	cursor.execute('CREATE TABLE cheese-country(chid INT, coid INT)')
	cursor.execute('CREATE TABLE cheese-recipes(chid INT, reid INT)')
	db.commit();


def db_exists(filename):
	from os.path import isfile, getsize

	if not isfile(filename):
		return False
	if getsize(filename) < 100:
		return False
	
	with open(filename, 'rb') as f:
		header = f.read(100)

	return header[:16] == 'SQLite format 3\x00'

def connect_cheese_country(cheese, country):
	cursor = db.cursor()

	cursor.execute('insert into cheese-country values (? ,?)',
		(cheese.get_id(), country.get_id()))

def connect_cheese_recipe(cheese, recipe):
	cursor = db.cursor()

	cursor.execute('insert into cheese-recipes values (? ,?)',
		(cheese.get_id(), recipe.get_id()))

def add_cheese_row(db, cheese):
	cursor = db.cursor()

	#first we add to cheese table
	cursor.execute('insert into cheeses values (?, ?)',
		(str(cheese.get_name()), str(cheese.get_softness())))

	#get the id sqlite automatically assigned
	cheese.set_id(cursor.lastrowid))

def del_cheese_row(db, cheese_to_del):
	cursor = db.cursor()
	
	cursor.execute("delete from cheeses where name = ?",
		(str(cheese_to_del.get_name()),))

	cursor.execute("delete from cheese-country where chid = ?",
		(cheese_to_del.get_id(),))

	cursor.execute("delete from cheese-recipes where chid = ?",
		(cheese_to_del.get_id(),))

def add_country_row(db, country):
	cursor = db.cursor()

	#first we add to country table
	cursor.execute('insert into countries values (?)',
		(str(country.get_name())))

	#get the id sqlite automatically assigned
	country.set_id(cursor.lastrowid))

def del_country_row(db, country_to_del):
	cursor = db.cursor()

	cursor.execute("delete from countries where name = ",
		(str(country_to_del.get_name()),))
	cursor.execute("delete from cheese-country where coid = ?",
		(country_to_del.get_id(),))

def add_recipe_row(db, recipe):
	cursor = db.cursor()

	#first we add to recipe table
	cursor.execute('insert into recipes values (?, ?, ?)',
		(str(recipe.get_name()), str(recipe.get_softness()),
		str(recipe.get_time())))

	#get the id sqlite automatically assigned
	recipe.set_id(cursor.lastrowid))

def del_recipe_row(db, recipe_to_del):
	cursor = db.cursor()

	cursor.execute("delete from recipes where name = ",
		(str(recipe_to_del.get_name()),))

	cursor.execute("delete from cheese-recipes where reid = ?",
		(recipe_to_del.get_id(),))

if db_exists('db/database'):
	db = sqlite3.connect('db/database')
	cursor = db.cursor()
else:
	db = sqlite3.connect("db/database")
	create_db(db)
	cursor = db.cursor()


	
db.close;
