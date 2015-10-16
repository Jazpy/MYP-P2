import unittest
import cheesedb
import table_objects
import sqlite3

class TestCDB(unittest.TestCase):

	def setUp(self):
		pass

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

	def test_table_object_country(self):
		x = table_objects.country(1, "a")
		
		self.assertEqual(x.get_id() == 1, True)
		self.assertEqual(x.get_name() == "a", True)

		x.set_id(2)
		self.assertEqual(x.get_id() == 2, True)
		x.set_name("b")
		self.assertEqual(x.get_name() == "b", True)
	
	def test_table_object_recipe(self):
		x = table_objects.recipe(1, "a", "b", 1)
		
		self.assertEqual(x.get_id() == 1, True)
		self.assertEqual(x.get_name() == "a", True)
		self.assertEqual(x.get_instructions() == "b", True)
		self.assertEqual(x.get_time() == 1, True)

		x.set_id(2)
		self.assertEqual(x.get_id() == 2, True)
		x.set_name("b")
		self.assertEqual(x.get_name() == "b", True)
		x.set_instructions("a")
		self.assertEqual(x.get_instructions() == "a", True)
		x.set_time(2)
		self.assertEqual(x.get_time() == 2, True)

if __name__ == '__main__':
	unittest.main()
