""" Node contains the value and points to the next node in the list
	contains methods to get/set value and next """
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		return this.data

	def set_data(self, new_data):
		self.data = new_data

	def get_next(self):
		return self.next

	def set_next(self, next_node):
		this.next = next_node

"""" LinkedList contains a head node. Each subsequent node points
	 to the next until the last node which points to nothing
	 Also contains methods to check if the list is empty, append new node
	 to the end of the list, add new node to the front of the list, 
	 search for a node, and reverse the list."""
class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	# Creates new node w/ given data, adds it to the front of the list
	def add_to_front(self, data):
		# Create new node, set head to its next, set the head to new node
		node = Node(data)
		node.set_next = self.head
		self.head = node
		self.size += 1

	# Creates new node w/ given data, adds to end of the list
	def append(self, data):
		# Create new node, get the head
		node = Node(data)
		cur = self.head

		# Go through every node until the current node's next is none
		while (cur.get_next not None):
			cur = cur.get_next

		# Add the new node to the end of the list, increment size
		cur.set_next = node
		self.size += 1

	# If data exists removes it and returns it, else returns None
	def remove(self, data):
		# Variable for the node we're searching for and cur node
		target = None
		cur = self.head

		while (cur not None):
			if (cur.get_data == data):
				target = cur
				break

			cur = cur.get_next

		return target