import unittest
import cheesedb
import table_objects
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
		cursor = self.db.cursor()

		cheesedb.add_cheese_row(self.db, "testcheese", "no", "no")

		cursor.execute(
			"select id from cheeses where name = 'testcheese'")
		exist = cursor.fetchone()

		self.assertEqual(exist is not None, True)

		cheesedb.del_cheese_row(self.db, "testcheese")

		cursor.execute(
			"select id from cheeses where name = 'testcheese'")
		exist = cursor.fetchone()

		self.assertEqual(exist is None, True)

	def test_country_table(self):
		cursor = self.db.cursor()

		cheesedb.add_country_row(self.db, "testcountry", "a, b")

		cursor.execute(
			"select id from countries where name = 'testcountry'")
		exist = cursor.fetchone()

		self.assertEqual(exist is not None, True)

		cheesedb.del_cheese_row(self.db, "testcountry")

		cursor.execute(
			"select id from countries where name = 'testcountry'")
		exist = cursor.fetchone()

		self.assertEqual(exist is None, True)

	def test_recipe_table(self):
		cursor = self.db.cursor()

		cheesedb.add_cheese_row(self.db, "testrecipe", "no", "no")

		cursor.execute(
			"select id from recipes where name = 'testrecipe'")
		exist = cursor.fetchone()

		self.assertEqual(exist is not None, True)

		cheesedb.del_cheese_row(self.db, "testrecipe")

		cursor.execute(
			"select id from recipes where name = 'testrecipe'")
		exist = cursor.fetchone()

		self.assertEqual(exist is None, True)

	def test_table_object_cheese(self):
		x = table_objects.cheese(1, "a", "b")
		
		self.assertEqual(x.get_id() == 1, True)
		self.assertEqual(x.get_name() == "a", True)
		self.assertEqual(x.get_softness() == "b", True)

		x.set_id(2)
		self.assertEqual(x.get_id() == 2, True)
		x.set_name("b")
		self.assertEqual(x.get_name() == "b", True)
		x.set_softness("a")
		self.assertEqual(x.get_softness() == "a", True)

if __name__ == '__main__':
	unittest.main()
