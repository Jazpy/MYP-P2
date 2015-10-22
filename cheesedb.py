import sqlite3
import Tkinter as tk
import db_func
from controller import controller
import table_objects

def main():
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
	
	print len(cursor.execute("select rowid from recipes").fetchall())

	db.commit()
	db.close();

if __name__ == "__main__":
	main()
