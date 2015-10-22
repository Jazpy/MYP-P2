import Tkinter as tk
import ttk
import textwrap
import db_func
import table_objects

class controller(tk.Frame):

	def __init__(self, parent, db):
		tk.Frame.__init__(self, parent, background = "white")
		
		self.parent = parent
		self.db = db
		self.init_ui()

		self.area1 = None
		self.area2 = None
		self.area3 = None
		self.area4 = None
		self.listbox = None

		self.main_menu("")

	def init_ui(self):
		self.parent.title("RECIPINATOR")
		self.pack(fill = tk.BOTH, expand = 1)

	def clean(self):
		for widget in self.winfo_children():
			widget.destroy()

		self.area1 = None
		self.area2 = None
		self.area3 = None
		self.area4 = None
		self.listbox = None

	def main_menu(self, event):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 1)

		add = ttk.Button(self, text = "Add", style = "Slate.TButton")
		add.grid(row = 0, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
        	delete = ttk.Button(self, text = "Delete", style = "Slate.TButton")
        	delete.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		search = ttk.Button(self, text = "Search", style = "Slate.TButton")
        	search.grid(row = 2, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		add.bind("<1>", self.add_menu)
		delete.bind("<1>", self.delete_menu)
		search.bind("<1>", self.search_menu)

		self.pack()

	def add_menu(self, event):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 1)

		cheese = ttk.Button(self, text = "Add cheese",
			style = "Slate.TButton")
		cheese.grid(row = 0, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
        	recipe = ttk.Button(self, text = "Add recipe",
			style = "Slate.TButton")
        	recipe.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 2, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		cheese.bind("<1>", self.add_cheese)
		recipe.bind("<1>", self.add_recipe)
		back.bind("<1>", self.main_menu)

		self.pack()

	def add_cheese(self, event):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 0)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 0)
		self.rowconfigure(3, pad = 3, weight = 1)
		self.rowconfigure(4, pad = 3, weight = 0)
		self.rowconfigure(5, pad = 3, weight = 1)
		self.rowconfigure(6, pad = 3, weight = 0)
		self.rowconfigure(7, pad = 3, weight = 0)

		clabel = tk.Label(self, text = "Name:", font = ("Arial", 16),
			bg = "white")
		clabel.grid(row = 0, column = 0)
		self.area1 = tk.Text(self)
		self.area1.grid(row = 1, column = 0, columnspan = 1,
			rowspan = 1)

		colabel = tk.Label(self, text = "Country of origin:",
			font = ("Arial", 16), bg = "white")
		colabel.grid(row = 2, column = 0)
		self.area2 = tk.Text(self)
		self.area2.grid(row = 3, column = 0, columnspan = 1,
			rowspan = 1)

		solabel = tk.Label(self, text = "Softness of cheese:",
			font = ("Arial", 16), bg = "white")
		solabel.grid(row = 4, column = 0)
		self.area3 = tk.Text(self)
		self.area3.grid(row = 5, column = 0, columnspan = 1,
			rowspan = 1)

		add = ttk.Button(self, text = "Add", style = "Slate.TButton")
		add.grid(row = 6, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back = ttk.Button(self, text = "Back", style = "Slate.TButton")
		back.grid(row = 7, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back.bind("<1>", self.add_menu)
		add.bind("<1>", self.db_add_cheese)

		self.pack()

	def db_add_cheese(self, event):
		cheese_name = self.area1.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')
		country_name = self.area2.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')
		softness = self.area3.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')

		cheese_to_add = None
		country_to_add = None

		if cheese_name != "":
			cheese_to_add = table_objects.cheese(-1,
				cheese_name, softness)
			db_func.add_cheese_row(self.db, cheese_to_add)
		if country_name != "":
			country_to_add = table_objects.country(-1,
				country_name)
			db_func.add_country_row(self.db, country_to_add)

		if cheese_to_add is not None and country_to_add is not None:
			db_func.connect_cheese_country(self.db,
				cheese_to_add, country_to_add)

		self.clean()

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)

		label = tk.Label(self, text = "Success!",
			font = ("Arial", 20), bg = "white")
		label.grid(row = 0, column = 0)

		back = ttk.Button(self, text = "Back", style = "Slate.TButton")
		back.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back.bind("<1>", self.main_menu)

		self.pack()

	def add_recipe(self, event):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 0)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 0)
		self.rowconfigure(3, pad = 3, weight = 1)
		self.rowconfigure(4, pad = 3, weight = 0)
		self.rowconfigure(5, pad = 3, weight = 1)
		self.rowconfigure(6, pad = 3, weight = 0)
		self.rowconfigure(7, pad = 3, weight = 1)
		self.rowconfigure(8, pad = 3, weight = 0)
		self.rowconfigure(9, pad = 3, weight = 0)

		clabel = tk.Label(self, text = "Cheese used:",
			font = ("Arial", 16), bg = "white")
		clabel.grid(row = 0, column = 0)
		self.area1 = tk.Text(self)
		self.area1.grid(row = 1, column = 0, columnspan = 1,
			rowspan = 1)

		relabel = tk.Label(self, text = "Recipe name:",
			font = ("Arial", 16), bg = "white")
		relabel.grid(row = 2, column = 0)
		self.area2 = tk.Text(self)
		self.area2.grid(row = 3, column = 0, columnspan = 1,
			rowspan = 1)

		tilabel = tk.Label(self, text = "Cooking time:",
			font = ("Arial", 16), bg = "white")
		tilabel.grid(row = 4, column = 0)
		self.area3 = tk.Text(self)
		self.area3.grid(row = 5, column = 0, columnspan = 1,
			rowspan = 1)

		inlabel = tk.Label(self, text = "Instructions:",
			font = ("Arial", 16), bg = "white")
		inlabel.grid(row = 6, column = 0)
		self.area4 = tk.Text(self)
		self.area4.grid(row = 7, column = 0, columnspan = 1,
			rowspan = 1)


		add = ttk.Button(self, text = "Add", style = "Slate.TButton")
		add.grid(row = 8, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		
		back = ttk.Button(self, text = "Back", style = "Slate.TButton")
		back.grid(row = 9, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back.bind("<1>", self.add_menu)
		add.bind("<1>", self.db_add_recipe)

		self.pack()

	def db_add_recipe(self, event):
		cheese_name = self.area1.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')
		recipe_name = self.area2.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')
		time = self.area3.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')
		instructions = self.area4.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)

		if (cheese_name == "" or recipe_name == ""):
			self.clean()

			label = tk.Label(self, text =
				"Error: A name field was left blank",
				font = ("Arial", 20), bg = "white")
			label.grid(row = 0, column = 0)

			back = ttk.Button(self, text = "Back",
				style = "Slate.TButton")
			back.grid(row = 1, column = 0,
				sticky = tk.N + tk.S + tk.E + tk.W)

			back.bind("<1>", self.main_menu)
		elif (db_func.row_exists(self.db, cheese_name, "cheeses") is False or
			db_func.row_exists(self.db, recipe_name, "recipes") is True):
			self.clean()

			label = tk.Label(self, text = 
				"Error: Cheese doesn't exist in database, "\
				"or recipe already exists",
				font = ("Arial", 16), bg = "white")
			label.grid(row = 0, column = 0)

			back = ttk.Button(self, text = "Back",
				style = "Slate.TButton")
			back.grid(row = 1, column = 0,
				sticky = tk.N + tk.S + tk.E + tk.W)

			back.bind("<1>", self.main_menu)
		else:
			cheese_to_add = table_objects.cheese(-1,
				cheese_name, "notimportant")
			db_func.add_cheese_row(self.db, cheese_to_add)

			recipe_to_add = table_objects.recipe(-1,
				recipe_name, instructions, time)
			db_func.add_recipe_row(self.db,
				recipe_to_add)

			db_func.connect_cheese_recipe(self.db,
				cheese_to_add, recipe_to_add)

			self.clean()

			label = tk.Label(self, text = "Success!",
				font = ("Arial", 20), bg = "white")
			label.grid(row = 0, column = 0)

			back = ttk.Button(self, text = "Back",
				style = "Slate.TButton")
			back.grid(row = 1, column = 0,
				sticky = tk.N + tk.S + tk.E + tk.W)

			back.bind("<1>", self.main_menu)

		self.pack()

	def delete_menu(self, event):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 1)

		cheese = ttk.Button(self, text = "Delete cheese",
			style = "Slate.TButton")
		cheese.grid(row = 0, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
        	recipe = ttk.Button(self, text = "Delete recipe",
			style = "Slate.TButton")
        	recipe.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 2, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		cheese.bind("<1>", self.del_cheese)
		recipe.bind("<1>", self.del_recipe)
		back.bind("<1>", self.main_menu)

		self.pack()

	def del_cheese(self, event):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 0)
		self.rowconfigure(1, pad = 3, weight = 1)

		clabel = tk.Label(self, text = "Name:", font = ("Arial", 16),
			bg = "white")
		clabel.grid(row = 0, column = 0)
		self.area1 = tk.Text(self)
		self.area1.grid(row = 1, column = 0, columnspan = 1,
			rowspan = 1)

		delb = ttk.Button(self, text = "Delete",
			style = "Slate.TButton")
		delb.grid(row = 6, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back = ttk.Button(self, text = "Back", style = "Slate.TButton")
		back.grid(row = 7, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back.bind("<1>", self.delete_menu)
		delb.bind("<1>", self.db_del_cheese)

		self.pack()

	def db_del_cheese(self, event):
		cheese_name = self.area1.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')

		cheese_to_add = None

		if (cheese_name == "" or
			row_exists(self.db, cheese_name, "cheeses") is False):
			self.clean()

			self.columnconfigure(0, pad = 3, weight = 1)
			self.rowconfigure(0, pad = 3, weight = 1)
			self.rowconfigure(1, pad = 3, weight = 1)

			label = tk.Label(self, text =
				"Error: Cheese not found",
				font = ("Arial", 20), bg = "white")
			label.grid(row = 0, column = 0)
	
			back = ttk.Button(self, text = "Back",
				style = "Slate.TButton")
			back.grid(row = 1, column = 0,
				sticky = tk.N + tk.S + tk.E + tk.W)

			back.bind("<1>", self.main_menu)

		else:
			cursor = self.db.cursor()
			cursor.execute("select rowid from cheeses where name = ?",
				(str(cheese_name),))
		
			chid = cursor.fetchone()[0]

			cursor.execute("select softness from cheeses where name = ?",
				(str(cheese_name),))
		
			softness = cursor.fetchone()[0]

			cheese_to_del = table_objects.cheese(chid,
				cheese_name, softness)

			db_func.del_cheese_row(self.db, cheese_to_del)

			self.columnconfigure(0, pad = 3, weight = 1)
			self.rowconfigure(0, pad = 3, weight = 1)
			self.rowconfigure(1, pad = 3, weight = 1)

			label = tk.Label(self, text = "Success!",
				font = ("Arial", 20), bg = "white")
			label.grid(row = 0, column = 0)
	
			back = ttk.Button(self, text = "Back",
				style = "Slate.TButton")
			back.grid(row = 1, column = 0,
				sticky = tk.N + tk.S + tk.E + tk.W)
	
			back.bind("<1>", self.main_menu)
	
		self.pack()

	def del_recipe(self, event):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 0)
		self.rowconfigure(1, pad = 3, weight = 1)

		clabel = tk.Label(self, text = "Recipe name:",
			font = ("Arial", 16), bg = "white")
		clabel.grid(row = 0, column = 0)
		self.area1 = tk.Text(self)
		self.area1.grid(row = 1, column = 0, columnspan = 1,
			rowspan = 1)

		delb = ttk.Button(self, text = "Delete", style = "Slate.TButton")
		delb.grid(row = 8, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		
		back = ttk.Button(self, text = "Back", style = "Slate.TButton")
		back.grid(row = 9, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back.bind("<1>", self.delete_menu)
		delb.bind("<1>", self.db_del_recipe)

		self.pack()

	def db_del_recipe(self, event):
		recipe_name = self.area1.get("1.0", 'end-1c').lower().encode('ascii', 'ignore')

		recipe_to_add = None

		if (recipe_name == "" or
			row_exists(self.db, recipe_name, "recipes") is False):
			self.clean()

			self.columnconfigure(0, pad = 3, weight = 1)
			self.rowconfigure(0, pad = 3, weight = 1)
			self.rowconfigure(1, pad = 3, weight = 1)

			label = tk.Label(self, text =
				"Error: Recipe not found",
				font = ("Arial", 20), bg = "white")
			label.grid(row = 0, column = 0)
	
			back = ttk.Button(self, text = "Back",
				style = "Slate.TButton")
			back.grid(row = 1, column = 0,
				sticky = tk.N + tk.S + tk.E + tk.W)

			back.bind("<1>", self.main_menu)

		else:
			cursor = self.db.cursor()
			cursor.execute("select rowid from recipes where name = ?",
				(str(recipe_name),))
		
			reid = cursor.fetchone()[0]

			recipe_to_del = table_objects.recipe(reid,
				recipe_name, "notimportant", "notimportant")

			db_func.del_recipe_row(self.db, recipe_to_del)

			self.columnconfigure(0, pad = 3, weight = 1)
			self.rowconfigure(0, pad = 3, weight = 1)
			self.rowconfigure(1, pad = 3, weight = 1)

			label = tk.Label(self, text = "Success!",
				font = ("Arial", 20), bg = "white")
			label.grid(row = 0, column = 0)
	
			back = ttk.Button(self, text = "Back",
				style = "Slate.TButton")
			back.grid(row = 1, column = 0,
				sticky = tk.N + tk.S + tk.E + tk.W)
	
			back.bind("<1>", self.main_menu)
	
		self.pack()

	def search_menu(self, event):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 1)
		self.rowconfigure(3, pad = 3, weight = 1)

		softness = ttk.Button(self, text = "Search cheese by softness",
			style = "Slate.TButton")
		softness.grid(row = 0, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
        	country = ttk.Button(self, text = "Search cheese by country",
			style = "Slate.TButton")
        	country.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		recipe = ttk.Button(self, text = "Search recipe by cheese",
			style = "Slate.TButton")
        	recipe.grid(row = 2, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 3, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		softness.bind("<1>", self.search_softness)
		country.bind("<1>", self.search_country)
		recipe.bind("<1>", self.search_recipe)
		back.bind("<1>", self.main_menu)

		self.pack()

	def search_softness(self, event):
		self.clean()
	
		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.columnconfigure(1, pad = 3, weight = 0)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 1)

		scrollbar = tk.Scrollbar(self)
		self.listbox = tk.Listbox(self, yscrollcommand = scrollbar.set)

		cursor = self.db.cursor()
		cursor.execute("select softness from cheeses")
		softnesses = cursor.fetchall()
		softnesses = sorted(set(softnesses))

		for s in softnesses:
			self.listbox.insert(tk.END, str(s[0]))		

		scrollbar.config(command = self.listbox.yview)	

		self.listbox.grid(row = 0, column = 0, sticky = tk.E + tk.W)
		scrollbar.grid(row = 0, column = 1, sticky = tk.N + tk.S)
		search = ttk.Button(self, text = "Search",
			style = "Slate.TButton")
        	search.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 2, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		search.bind("<1>", self.show_search_softness)
		back.bind("<1>", self.search_menu)

		self.pack()

	def show_search_softness(self, event):
		sel_soft = self.listbox.get(tk.ACTIVE)
		
		self.clean()
	
		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.columnconfigure(1, pad = 3, weight = 0)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)

		scrollbar = tk.Scrollbar(self)
		self.listbox = tk.Listbox(self, yscrollcommand = scrollbar.set)

		cursor = self.db.cursor()
		cursor.execute("select name from cheeses where softness = ?",
			(str(sel_soft),))
		cheeses = cursor.fetchall()
		cheeses = sorted(set(cheeses))

		for s in cheeses:
			self.listbox.insert(tk.END, str(s[0]))		

		scrollbar.config(command = self.listbox.yview)	

		self.listbox.grid(row = 0, column = 0, sticky = tk.E + tk.W)
		scrollbar.grid(row = 0, column = 1, sticky = tk.N + tk.S)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back.bind("<1>", self.search_menu)

		self.pack()

	def search_country(self, event):
		self.clean()
	
		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.columnconfigure(1, pad = 3, weight = 0)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 1)

		scrollbar = tk.Scrollbar(self)
		self.listbox = tk.Listbox(self, yscrollcommand = scrollbar.set)

		cursor = self.db.cursor()
		cursor.execute("select name from countries")
		countries = cursor.fetchall()
		countries = sorted(set(countries))

		for s in countries:
			self.listbox.insert(tk.END, str(s[0]))		

		scrollbar.config(command = self.listbox.yview)	

		self.listbox.grid(row = 0, column = 0, sticky = tk.E + tk.W)
		scrollbar.grid(row = 0, column = 1, sticky = tk.N + tk.S)
		search = ttk.Button(self, text = "Search",
			style = "Slate.TButton")
        	search.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 2, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		search.bind("<1>", self.show_search_country)
		back.bind("<1>", self.search_menu)

		self.pack()

	def show_search_country(self, event):
		sel_country = self.listbox.get(tk.ACTIVE)
		
		self.clean()
	
		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.columnconfigure(1, pad = 3, weight = 0)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)

		scrollbar = tk.Scrollbar(self)
		self.listbox = tk.Listbox(self, yscrollcommand = scrollbar.set)

		cursor = self.db.cursor()
		cursor.execute("select rowid from countries where name = ?",
			(str(sel_country),))
		coid = cursor.fetchone()[0]
		cursor.execute("select chid from cheese_country where coid = ?",
			(str(coid),))
		chids = cursor.fetchall()
		
		cheeses = []	
	
		for chid in chids:
			cursor.execute("select name from cheeses where rowid = ?",
				(str(chid[0]),))

			cheeses.append(cursor.fetchone()[0])

		cheeses = sorted(set(cheeses))

		for s in cheeses:
			self.listbox.insert(tk.END, str(s))		

		scrollbar.config(command = self.listbox.yview)	

		self.listbox.grid(row = 0, column = 0, sticky = tk.E + tk.W)
		scrollbar.grid(row = 0, column = 1, sticky = tk.N + tk.S)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back.bind("<1>", self.search_menu)

		self.pack()

	def search_recipe(self, event):
		self.clean()
	
		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.columnconfigure(1, pad = 3, weight = 0)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 1)

		scrollbar = tk.Scrollbar(self)
		self.listbox = tk.Listbox(self, yscrollcommand = scrollbar.set)

		cursor = self.db.cursor()
		cursor.execute("select name from cheeses")
		cheeses = cursor.fetchall()
		cheeses = sorted(set(cheeses))

		for s in cheeses:
			self.listbox.insert(tk.END, str(s[0]))		

		scrollbar.config(command = self.listbox.yview)	

		self.listbox.grid(row = 0, column = 0, sticky = tk.E + tk.W)
		scrollbar.grid(row = 0, column = 1, sticky = tk.N + tk.S)
		search = ttk.Button(self, text = "Search",
			style = "Slate.TButton")
        	search.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 2, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		search.bind("<1>", self.show_search_recipe)
		back.bind("<1>", self.search_menu)

		self.pack()

	def show_search_recipe(self, event):
		sel_cheese = self.listbox.get(tk.ACTIVE)
		
		self.clean()
	
		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.columnconfigure(1, pad = 3, weight = 0)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 1)

		scrollbar = tk.Scrollbar(self)
		self.listbox = tk.Listbox(self, yscrollcommand = scrollbar.set)

		cursor = self.db.cursor()
		cursor.execute("select rowid from cheeses where name = ?",
			(str(sel_cheese),))
		chid = cursor.fetchone()[0]
		cursor.execute("select reid from cheese_recipes where chid = ?",
			(str(chid),))
		reids = cursor.fetchall()
		
		recipes = []	
	
		for reid in reids:
			cursor.execute("select name from recipes where rowid = ?",
				(str(reid[0]),))

			recipes.append(cursor.fetchone()[0])

		recipes = sorted(set(recipes))

		for s in recipes:
			self.listbox.insert(tk.END, str(s))		

		scrollbar.config(command = self.listbox.yview)	

		self.listbox.grid(row = 0, column = 0, sticky = tk.E + tk.W)
		scrollbar.grid(row = 0, column = 1, sticky = tk.N + tk.S)
		details = ttk.Button(self, text = "Details",
			style = "Slate.TButton")
        	details.grid(row = 1, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)
		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 2, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		details.bind("<1>", self.show_recipe_details)
		back.bind("<1>", self.search_recipe)

		self.pack()

	def show_recipe_details(self, event):
		sel_recipe = self.listbox.get(tk.ACTIVE)
		
		self.clean()
	
		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")
			foreground = "black", background = "white")

		self.columnconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(0, pad = 3, weight = 1)
		self.rowconfigure(1, pad = 3, weight = 1)
		self.rowconfigure(2, pad = 3, weight = 4)
		self.rowconfigure(3, pad = 3, weight = 1)

		cursor = self.db.cursor()
		cursor.execute("select time from recipes where name = ?",
			(str(sel_recipe),))
		time = cursor.fetchone()[0]

		cursor.execute("select instructions from " \
			"recipes where name = ?",
			(str(sel_recipe),))
		instructions = cursor.fetchone()[0]

		nlabel = tk.Label(self, text = sel_recipe,
			font = ("Arial", 16), bg = "white",
			anchor = tk.W, justify = tk.LEFT)
		nlabel.grid(row = 0, column = 0)
		tlabel = tk.Label(self, text = time,
			font = ("Arial", 12), bg = "white",
			anchor = tk.W, justify = tk.LEFT)
		tlabel.grid(row = 1, column = 0)
		ilabel = tk.Label(self, text = instructions,
			font = ("Arial", 12), bg = "white",
			anchor = tk.W, justify = tk.LEFT)
		ilabel.grid(row = 2, column = 0)


		back = ttk.Button(self, text = "Back",
			style = "Slate.TButton")
        	back.grid(row = 3, column = 0,
			sticky = tk.N + tk.S + tk.E + tk.W)

		back.bind("<1>", self.search_recipe)

		self.pack()

