""" Node contains the value and points to the next node in the list
	contains methods to get/set value and next """
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

	# Getter for data
	def get_data(self):
		return this.data

	# Setter for data
	def set_data(self, new_data):
		self.data = new_data

	# Getter for next
	def get_next(self):
		return self.next

	# Setter for next
	def set_next(self, next_node):
		this.next = next_node

	# To string methods
	def __str__(self):
		return str(self.data)