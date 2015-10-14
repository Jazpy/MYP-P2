import unittest
import cheesedb
import sqlite3

class TestCDB(unittest.TestCase):

	def setUp(self):
		if cheesedb.db_exists('db/database'):
			self.db = sqlite3.connect("db/database")
		else:
			self.db = sqlite3.connect("db/database")
			cheesedb.create_db(self.db)

	def tearDown(self):
		self.db.close()

	def test_db_exists(self):
		self.assertEqual(cheesedb.db_exists('db/database'), True)

	def test_cheese_table(self):
		cursor = self.db.cursor

		cheesedb.add_cheese_row(self.db, "testcheese, no, no")

		cursor.execute("select rowid from cheeses where name = "
			"testcheese")
		exist = cursor.fetchone()

		self.assertEqual(exist is not None, True)

		cheesedb.del_cheese_row(self.db, "testcheese")

		cursor.execute("select rowid from cheeses where name = "
			"testcheese")
		exist = cursor.fetchone()

		self.assertEqual(exist is None, True)

	def test_country_table(self):
		cursor = self.db.cursor

		cheesedb.add_cheese_row(self.db, "testcountry, no, no")

		cursor.execute("select rowid from countries where name = "
			"testcountry")
		exist = cursor.fetchone()

		self.assertEqual(exist is not None, True)

		cheesedb.del_cheese_row(self.db, "testcountry")

		cursor.execute("select rowid from countries where name = "
			"testcountry")
		exist = cursor.fetchone()

		self.assertEqual(exist is None, True)

	def test_recipe_table(self):
		cursor = self.db.cursor

		cheesedb.add_cheese_row(self.db, "testrecipe, no, no")

		cursor.execute("select rowid from recipes where name = "
			"testrecipe")
		exist = cursor.fetchone()

		self.assertEqual(exist is not None, True)

		cheesedb.del_cheese_row(self.db, "testrecipe")

		cursor.execute("select rowid from recipes where name = "
			"testrecipe")
		exist = cursor.fetchone()

		self.assertEqual(exist is None, True)

if __name__ == '__main__':
	unittest.main()
