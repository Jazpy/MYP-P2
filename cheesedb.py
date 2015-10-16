import sqlite3
import table_objects

def create_db(db):
	cursor = db.cursor()
	cursor.execute('CREATE TABLE cheeses(name TEXT, softness TEXT)')
	cursor.execute('CREATE TABLE countries(name TEXT)')
	cursor.execute('''CREATE TABLE recipes(name TEXT, instructions TEXT,
		time TEXT)''')
	cursor.execute('CREATE TABLE cheese_country(chid INT, coid INT)')
	cursor.execute('CREATE TABLE cheese_recipes(chid INT, reid INT)')
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

	cursor.execute('insert into cheese_country values (? ,?)',
		(cheese.get_id(), country.get_id()))

def connect_cheese_recipe(cheese, recipe):
	cursor = db.cursor()

	cursor.execute('insert into cheese_recipes values (? ,?)',
		(cheese.get_id(), recipe.get_id()))

def add_cheese_row(db, cheese):
	cursor = db.cursor()

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

if db_exists('db/database'):
	db = sqlite3.connect('db/database')
	cursor = db.cursor()
else:
	db = sqlite3.connect("db/database")
	create_db(db)
	cursor = db.cursor()

ch1 = table_objects.cheese(None, "Provoleta", "hard")
ch2 = table_objects.cheese(None, "Gouda", "semi-soft")
ch3 = table_objects.cheese(None, "Brie", "soft")

co1 = table_objects.country(None, "Italy")
co2 = table_objects.country(None, "Netherlands")
co3 = table_objects.country(None, "France")

re1 = table_objects.recipe(None, "Provoleta crackers",
	"put em on top", "1 min")
re2 = table_objects.recipe(None, "Gouda spaghetti",
	"mix it in", "15 min")
re3 = table_objects.recipe(None, "Brie cake",
	"bake it", "2 hours")

print(ch1.get_id())
print(ch2.get_id())
print(ch3.get_id())

add_cheese_row(db, ch1)
add_cheese_row(db, ch2)
add_cheese_row(db, ch3)

print(ch1.get_id())
print(ch2.get_id())
print(ch3.get_id())

print(co1.get_id())
print(co2.get_id())
print(co3.get_id())

add_country_row(db, co1)
add_country_row(db, co2)
add_country_row(db, co3)

print(co1.get_id())
print(co2.get_id())
print(co3.get_id())

print(re1.get_id())
print(re2.get_id())
print(re3.get_id())

add_recipe_row(db, re1)
add_recipe_row(db, re2)
add_recipe_row(db, re3)

print(re1.get_id())
print(re2.get_id())
print(re3.get_id())

connect_cheese_country(ch1, co1)
connect_cheese_country(ch2, co2)
connect_cheese_country(ch3, co3)

connect_cheese_recipe(ch1, re1)
connect_cheese_recipe(ch2, re2)
connect_cheese_recipe(ch3, re3)

cursor.execute("Select * from cheeses")
print(cursor.fetchall())

cursor.execute("Select * from countries")
print(cursor.fetchall())

cursor.execute("Select * from recipes")
print(cursor.fetchall())

cursor.execute("Select * from cheese_country")
print(cursor.fetchall())

cursor.execute("Select * from cheese_recipes")
print(cursor.fetchall())

db.commit()
db.close();
