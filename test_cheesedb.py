import unittest
import cheesedb

class TestCDB(unittest.TestCase):

	def setUp(self):
		pass

	def test_db_exists(self):
		self.assertEqual(cheesedb.db_exists('db/database'), True)

	def test_add_cheese_row(self):
		self.assertEqual(True, True)

	def test_del_cheese_row(self):
		self.assertEqual(True, True)

	def test_add_country_row(self):
		self.assertEqual(True, True)

	def test_del_country_row(self):
		self.assertEqual(True, True)

	def test_add_recipe_row(self):
		self.assertEqual(True, True)

	def test_del_recipe_row(self):
		self.assertEqual(True, True)


if __name__ == '__main__':
	unittest.main()
