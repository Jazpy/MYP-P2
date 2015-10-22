import sqlite3

"""
This module handles sqlite3 commands
"""

def create_db(db):
	"""
	Creates tables in database

	:param db: database to fill
	:return: returns nothing
	"""

	cursor = db.cursor()
	cursor.execute('CREATE TABLE cheeses(name TEXT, softness TEXT)')
	cursor.execute('CREATE TABLE countries(name TEXT)')
	cursor.execute('''CREATE TABLE recipes(name TEXT, instructions TEXT,
		time TEXT)''')
	cursor.execute('CREATE TABLE cheese_country(chid INT, coid INT)')
	cursor.execute('CREATE TABLE cheese_recipes(chid INT, reid INT)')
	db.commit();

def row_exists(db, name, table):
	"""
	Checks if row exists

	:param db: database to use
	:param name: name to check
	:param table: tabletabase to use
	:return: returns nothing
	"""
	
	cursor = db.cursor()
	cursor.execute("select rowid from %s where name = ?" %(str(table)), (str(name),))

	exist = cursor.fetchone()
	
	if exist is None:
		return False

	return True

def db_exists(filename):
	"""
	Checks if database exists

	:param filename: filename of database to check
	:return: returns True if database exists and is sqlite3 database,
		false otherwise
	"""
	
	from os.path import isfile, getsize

	if not isfile(filename):
		return False
	if getsize(filename) < 100:
		return False
	
	with open(filename, 'rb') as f:
		header = f.read(100)

	return header[:16] == 'SQLite format 3\x00'

def connect_cheese_country(db, cheese, country):
	"""
	Connects cheese to country in relation table

	:param db: database to use
	:param cheese: cheese to connect
	:param country: country to connect
	:return: returns nothing
	"""	
	cursor = db.cursor()

	cursor.execute("select * from cheese_country where chid = ? and coid = ?",
		(str(cheese.get_id()), str(country.get_id())))

	if cursor.fetchone() is not None:
		return

	cursor.execute('insert into cheese_country values (? ,?)',
		(cheese.get_id(), country.get_id()))

def connect_cheese_recipe(db, cheese, recipe):
	"""
	Connects cheese to recipe in relation table

	:param db: database to use
	:param cheese: cheese to connect
	:param recipe: recipe to connect
	:return: returns nothing
	"""
	
	cursor = db.cursor()

	cursor.execute("select * from cheese_recipes where chid = ? and reid = ?",
		(str(cheese.get_id()), str(recipe.get_id())))

	if cursor.fetchone() is not None:
		return

	cursor.execute('insert into cheese_recipes values (? ,?)',
		(cheese.get_id(), recipe.get_id()))

def add_cheese_row(db, cheese):
	"""
	Adds cheese row

	:param db: database to use
	:param cheese: cheese to add
	:return: returns nothing
	"""		
	cursor = db.cursor()
	
	if row_exists(db, cheese.get_name(), "cheeses") is True:
		cursor.execute("select rowid from cheeses where name = ?", (str(cheese.get_name()),))
		cheese.set_id(cursor.fetchone()[0])

		return


	#first we add to cheese table
	cursor.execute('insert into cheeses values (?, ?)',
		(str(cheese.get_name()), str(cheese.get_softness())))

	#get the id sqlite automatically assigned
	cheese.set_id(cursor.lastrowid)

def del_cheese_row(db, cheese_to_del):
	"""
	Deletes cheese row

	:param db: database to use
	:param cheese_to_del: cheese to delete
	:return: returns nothing
	"""	
	cursor = db.cursor()

	cursor.execute("select coid from cheese_country where chid = ?",
		(str(cheese_to_del.get_id()),))

	coid = cursor.fetchone()[0]
	cursor.execute("select chid from cheese_country where coid = ?",
		(str(coid),))

	if len(cursor.fetchall()) == 1:
		cursor.execute("delete from countries where rowid = ?",
			(str(coid),))

	cursor.execute("select reid from cheese_recipes where chid = ?",
		(str(cheese_to_del.get_id()),))

	recipes = cursor.fetchall()

	for row in recipes:
		cursor.execute("delete from recipes where rowid = ?",
			(str(row[0]),))
	
	cursor.execute("delete from cheeses where name = ?",
		(str(cheese_to_del.get_name()),))

	cursor.execute("delete from cheese_country where chid = ?",
		(cheese_to_del.get_id(),))

	cursor.execute("delete from cheese_recipes where chid = ?",
		(cheese_to_del.get_id(),))
	

def add_country_row(db, country):
	"""
	Adds country row

	:param db: database to use
	:param country: country to add
	:return: returns nothing
	"""
	
	cursor = db.cursor()
	
	if row_exists(db, country.get_name(), "countries") is True:
		cursor.execute("select rowid from countries where name = ?", (str(country.get_name()),))
		country.set_id(cursor.fetchone()[0])

		return

	#first we add to country table
	cursor.execute('insert into countries values (?)',
		(str(country.get_name()),))

	#get the id sqlite automatically assigned
	country.set_id(cursor.lastrowid)

def del_country_row(db, country_to_del):
	"""
	Deletes country row

	:param db: database to use
	:param country_to_del: country to delete
	:return: returns nothing
	"""
	
	cursor = db.cursor()

	cursor.execute("delete from countries where name = ",
		(str(country_to_del.get_name()),))
	cursor.execute("delete from cheese_country where coid = ?",
		(country_to_del.get_id(),))

def add_recipe_row(db, recipe):
	"""
	Adds recipe row

	:param db: database to use
	:param recipe: recipe to add
	:return: returns nothing
	"""	
	cursor = db.cursor()
	
	if row_exists(db, recipe.get_name(), "recipes") is True:
		cursor.execute("select rowid from recipes where name = ?", (str(recipe.get_name()),))
		recipe.set_id(cursor.fetchone()[0])

		return

	#first we add to recipe table
	cursor.execute('insert into recipes values (?, ?, ?)',
		(str(recipe.get_name()), str(recipe.get_instructions()),
		str(recipe.get_time())))

	#get the id sqlite automatically assigned
	recipe.set_id(cursor.lastrowid)

def del_recipe_row(db, recipe_to_del):
	"""
	Deletes recipe row

	:param db: database to use
	:param recipe_to_del: recipe to delete
	:return: returns nothing
	"""
	
	cursor = db.cursor()

	cursor.execute("delete from recipes where name = ?",
		(str(recipe_to_del.get_name()),))

	cursor.execute("delete from cheese_recipes where reid = ?",
		(recipe_to_del.get_id(),))
