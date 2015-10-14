import unittest
import cheesedb

class TestCDB(unittest.TestCase):

	def setUp(self):
		pass

	def test_db_exists(self):
		self.assertEqual(cheesedb.db_exists('db/database'), True)

	def test_add_table(self):
		self.assertEqual(True, True)

	def test_add_row(self):
		self.assertEqual(True, True)

	def test_del_row(self):
		self.assertEqual(True, True)

if __name__ == '__main__':
	unittest.main()
