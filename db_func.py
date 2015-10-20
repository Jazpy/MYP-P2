import sqlite3

def create_db(db):
	cursor = db.cursor()
	cursor.execute('CREATE TABLE cheeses(name TEXT, softness TEXT)')
	cursor.execute('CREATE TABLE countries(name TEXT)')
	cursor.execute('''CREATE TABLE recipes(name TEXT, instructions TEXT,
		time TEXT)''')
	cursor.execute('CREATE TABLE cheese_country(chid INT, coid INT)')
	cursor.execute('CREATE TABLE cheese_recipes(chid INT, reid INT)')
	db.commit();

def row_exists(db, name, table):
	cursor = db.cursor()
	cursor.execute("select rowid from %s where name = ?" %(str(table)), (str(name),))

	exist = cursor.fetchone()
	
	if exist is None:
		return False

	return True

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

	cursor.execute("select * from cheese_country where chid = ? and coid = ?",
		(str(cheese.get_id()), str(country.get_id())))

	if cursor.fetchone() is not None:
		return

	cursor.execute('insert into cheese_country values (? ,?)',
		(cheese.get_id(), country.get_id()))

def connect_cheese_recipe(cheese, recipe):
	cursor = db.cursor()

	cursor.execute("select * from cheese_recipes where chid = ? and reid = ?",
		(str(cheese.get_id()), str(recipe.get_id())))

	if cursor.fetchone() is not None:
		return

	cursor.execute('insert into cheese_recipes values (? ,?)',
		(cheese.get_id(), recipe.get_id()))

def add_cheese_row(db, cheese):
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
	cursor = db.cursor()
	
	cursor.execute("delete from cheeses where name = ?",
		(str(cheese_to_del.get_name()),))

	cursor.execute("delete from cheese_country where chid = ?",
		(cheese_to_del.get_id(),))

	cursor.execute("delete from cheese_recipes where chid = ?",
		(cheese_to_del.get_id(),))

def add_country_row(db, country):
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
	cursor = db.cursor()

	cursor.execute("delete from countries where name = ",
		(str(country_to_del.get_name()),))
	cursor.execute("delete from cheese_country where coid = ?",
		(country_to_del.get_id(),))

def add_recipe_row(db, recipe):
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
	cursor = db.cursor()

	cursor.execute("delete from recipes where name = ",
		(str(recipe_to_del.get_name()),))

	cursor.execute("delete from cheese_recipes where reid = ?",
		(recipe_to_del.get_id(),))

def search_by_country(db, name):
	cursor = db.cursor()
	
	cursor.execute("select rowid from countries where name = ?", (str(name),))
	desired_id = cursor.fetchone()[0]

	cursor.execute("select chid from cheese_country where coid = ?", (str(desired_id),))
	rows = cursor.fetchall()

	print desired_id
	for row in rows:
		cursor.execute("select name,softness from cheeses where rowid = ?", (str(row[0]),))
		selected_cheeses = cursor.fetchall()

		for c in selected_cheeses:
			print c[0], c[1]

def search_by_recipe(db, name):
	cursor = db.cursor()
	
	cursor.execute("select rowid from recipes where name = ?", (str(name),))
	desired_id = cursor.fetchone()[0]

	cursor.execute("select chid from cheese_recipes where reid = ?", (str(desired_id),))
	rows = cursor.fetchall()

	print desired_id
	for row in rows:
		cursor.execute("select name,softness from cheeses where rowid = ?", (str(row[0]),))
		selected_cheeses = cursor.fetchall()

		for c in selected_cheeses:
			print c[0], c[1]

def search_by_softness(db, softness):
	cursor = db.cursor()
	to_print = ""
	
	cursor.execute("select rowid from cheeses where softness = ?", (str(softness),))
	desired_ids = cursor.fetchall()

	for cid in desired_ids:
		to_print += "cheese: "
	
		cursor.execute("select name from cheeses where rowid = ?", (str(cid[0]),))
		to_print += cursor.fetchone()[0]

		cursor.execute("select coid from cheese_country where chid = ?", (str(cid[0]),))
		country_id = cursor.fetchone()[0]
		cursor.execute("select name from countries where rowid = ?", (str(country_id),))
		to_print += ", country: " + cursor.fetchone()[0]

		cursor.execute("select reid from cheese_recipes where chid = ?", (str(cid[0]),))
		recipe_ids = cursor.fetchall()
		to_print += ", recipes: "

		for recipe in recipe_ids:
			cursor.execute("select name from recipes where rowid = ?", (str(recipe[0]),))
			to_print += cursor.fetchone()[0] + ", "

		to_print = to_print[:-2]
		to_print += "\n"

	print to_print

def search_by_name(db, name):
	cursor = db.cursor()
	to_print = ""
	
	cursor.execute("select rowid from cheeses where name = ?", (str(name),))
	desired_ids = cursor.fetchall()

	for cid in desired_ids:
		to_print += "softness: "
	
		cursor.execute("select softness from cheeses where rowid = ?", (str(cid[0]),))
		to_print += cursor.fetchone()[0]

		cursor.execute("select coid from cheese_country where chid = ?", (str(cid[0]),))
		country_id = cursor.fetchone()[0]
		cursor.execute("select name from countries where rowid = ?", (str(country_id),))
		to_print += ", country: " + cursor.fetchone()[0]

		cursor.execute("select reid from cheese_recipes where chid = ?", (str(cid[0]),))
		recipe_ids = cursor.fetchall()
		to_print += ", recipes: "

		for recipe in recipe_ids:
			cursor.execute("select name from recipes where rowid = ?", (str(recipe[0]),))
			to_print += cursor.fetchone()[0] + ", "

		to_print = to_print[:-2]
		to_print += "\n"

	print to_print


