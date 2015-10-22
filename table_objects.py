"""
This module contains cheese, country, and recipe objects used by other modules
"""

class cheese:

	def __init__(self, init_id, init_name, init_softness):
		"""
		Initialize cheese object
		
		:param init_id: initial id
		:param init_name: initial name
		:param init_softness: initial softness
		:return: returns nothing
		"""
		self.id = init_id
		self.name = init_name
		self.softness = init_softness

	def get_id(self):
		"""
		Get cheese's id
		
		:return: returns cheeses's id
		"""
		return self.id

	def get_name(self):
		"""
		Get cheese name
		
		:return: returns cheeses's name
		"""
		return self.name

	def get_softness(self):
		"""
		Get cheese softness
		
		:return: returns cheeses's softness
		"""
		return self.softness

	def set_id(self, new_id):
		"""
		Set cheese's id
		
		:param new_id: new id
		:return: returns nothing
		"""
		self.id = new_id

	def set_name(self, new_name):
		"""
		Set cheese's name
		
		:param new_name: new name
		:return: returns nothing
		"""
		self.name = new_name
		
	def set_softness(self, new_softness):
		"""
		Set cheese's softness
		
		:param new_softness: new softness
		:return: returns nothing
		"""
		self.softness = new_softness
class country:

	def __init__(self, init_id, init_name):
		"""
		Initialize country object
		
		:param init_id: initial id
		:param init_name: initial name
		:return: returns nothing
		"""
		self.id = init_id
		self.name = init_name

	def get_id(self):
		"""
		Get country's id
		
		:return: returns country's id
		"""
		return self.id

	def get_name(self):
		"""
		Get country's name
		
		:return: returns country's name
		"""
		return self.name

	def set_id(self, new_id):
		"""
		Set country's id
		
		:param new_id: new id
		:return: returns nothing
		"""
		self.id = new_id

	def set_name(self, new_name):
		"""
		Set country's name
		
		:param new_name: new name
		:return: returns nothing
		"""
		self.name = new_name

class recipe:

	def __init__(self, init_id, init_name, init_instructions, init_time):
		"""
		Initialize recipe object
		
		:param init_id: initial id
		:param init_name: initial name
		:param init_instructions: initial instructions
		:param init_time: initial time
		:return: returns nothing
		"""
		self.id = init_id
		self.name = init_name
		self.instructions = init_instructions
		self.time = init_time

	def get_id(self):
		"""
		Get recipe's id
		
		:return: returns recipe's id
		"""
		return self.id
		
	def get_name(self):
		"""
		Get recipe's name
		
		:return: returns recipe's named
		"""
		return self.name

	def get_instructions(self):
		"""
		Get recipe's instructions		

		:return: returns recipe's instructions
		"""
		return self.instructions

	def get_time(self):
		"""
		Get recipe time
		
		:return: returns recipe's time
		"""
		return self.time

	def set_id(self, new_id):
		"""
		Set recipe's id
		
		:param new_id: new id
		:return: returns nothing
		"""
		self.id = new_id

	def set_name(self, new_name):
		"""
		Set recipe's name
		
		:param new_id: new name
		:return: returns nothing
		"""
		self.name = new_name

	def set_instructions(self, new_instructions):
		"""
		Set recipe's instructions
		
		:param new_id: new instructions
		:return: returns nothing
		"""
		self.instructions = new_instructions
		
	def set_time(self, new_time):
		"""
		Set recipe's time
		
		:param new_id: new time
		:return: returns nothing
		"""
		self.time = new_time
