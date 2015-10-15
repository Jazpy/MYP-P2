class cheese:

	def __init__(self, init_id, init_name, init_softness):
		self.id = init_id
		self.name = init_name
		self.softness = init_softness

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_softness(self):
		return self.softness

	def set_id(self, new_id):
		self.id = new_id

	def set_name(self, new_name):
		self.name = new_name
		
	def set_softness(self, new_softness):
		self.softness = new_softness
class country:

	def __init__(self, init_id, init_name):
		self.id = init_id
		self.name = init_name

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def set_id(self, new_id):
		self.id = new_id

	def set_name(self, new_name):
		self.name = new_name

class recipe:

	def __init__(self, init_id, init_name, init_instructions, init_time):
		self.id = init_id
		self.name = init_name
		self.instructions = init_instructions
		self.time = init_time

	def get_id(self):
		return self.id
		
	def get_name(self):
		return self.name

	def get_instructions(self):
		return self.instructions

	def get_time(self):
		return self.time

	def set_id(self, new_id):
		self.id = new_id

	def set_name(self, new_name):
		self.name = new_name

	def set_instructions(self, new_instructions):
		self.instructions = new_instructions
		
	def set_time(self, new_time):
		self.time = new_time
