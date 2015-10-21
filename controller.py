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
		cheese_name = self.area1.get("1.0", 'end-1c').lower()
		country_name = self.area2.get("1.0", 'end-1c').lower()
		softness = self.area3.get("1.0", 'end-1c').lower()

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
		cheese_name = self.area1.get("1.0", 'end-1c').lower()
		recipe_name = self.area2.get("1.0", 'end-1c').lower()
		time = self.area3.get("1.0", 'end-1c').lower()
		instructions = self.area4.get("1.0", 'end-1c').lower()

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
		print "del"

	def search_menu(self, event):
		print "sea"
