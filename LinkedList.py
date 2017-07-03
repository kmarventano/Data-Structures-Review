from Node import Node
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

		# If the list is empty, new node is the head
		if (cur == None):
			self.head = node

		else:
			# Go through every node until the current node's next is none
			while (cur.get_next != None):
				cur = cur.get_next

				# Add the new node to the end of the list, increment size
				cur.set_next = node
				self.size += 1


	# If data exists removes it and returns it, else returns None
	def remove(self, data):
		# Variable for the node we're searching for and cur node
		target = None
		cur = self.head

		while (cur != None):
			if (cur.get_data == data):
				target = cur
				break

			cur = cur.get_next

		return target

	# Searches for given data in list, true if in, false otherwise
	def contains(self, data):
		# Start at the head of the list
		cur = self.head

		# Go through every node until the end of the list
		while (cur != None):
			# If the node is found, return true, else  get the next node
			if (cur.get_data == data):
				return True

			else: 
				cur = cur.get_next

		# If we're here, we didn't find the node
		return False

	# Reverses the linked list iteratively
	def reverse(self):
		# Set the cur node to head, prev/next to none
		cur = self.head
		prev = None
		next = None

		# Go through entire list
		while (cur != None):
			next = cur.get_next
			cur.next = prev
			prev = cur
			cur = next
