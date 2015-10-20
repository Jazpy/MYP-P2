import Tkinter as tk
import ttk
import db_func

class controller(tk.Frame):

	def __init__(self, parent, db):
		tk.Frame.__init__(self, parent, background = "white")
		
		self.parent = parent
		self.db = db
		self.init_ui()

		self.main_menu()

	def init_ui(self):
		self.parent.title("RECIPINATOR")
		self.pack(fill = tk.BOTH, expand = 1)

	def clean(self):
		for widget in self.winfo_children():
			widget.destroy()

	def main_menu(self):
		self.clean()

		ttk.Style().configure("Slate.TButton", padding = 
			(0, 5, 0, 5), font = 'Arial 20',
			# foreground = "#CCCECF", background = "#092E3B")	
			forground = "black", background = "white")

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
		db_func.search_by_name(self.db, "Brie")

	def delete_menu(self, event):
		print "del"

	def search_menu(self, event):
		print "sea"
