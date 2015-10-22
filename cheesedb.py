import sqlite3
import Tkinter as tk
import db_func
from controller import controller
import table_objects

"""
This module only checks if database exists, and then launches the app's GUI,
finally, it saves any changes made to the database
"""

def main():
	"""
	Check if database exists, then launch app window

	:return: returns nothing
	"""
	if db_func.db_exists('db/database'):
		db = sqlite3.connect('db/database')
		cursor = db.cursor()
	else:
		db = sqlite3.connect("db/database")
		db_func.create_db(db)
		cursor = db.cursor()

	root = tk.Tk()
	root.geometry("640x480+10+10")
	app = controller(root, db)
	root.mainloop()

	db.commit()
	db.close();

if __name__ == "__main__":
	main()
