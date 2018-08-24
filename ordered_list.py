class Node:
	def __init__(self, v):
		self.value = v
		self.prev = None
		self.next = None

class OrderedList:
	def __init__(self, sort_ascending = True):
		self.head = None
		self.tail = None
		self.sort_ascending = sort_ascending

	def print_all_nodes(self):
		node = self.head
		while node != None:
			print(node.value)
			node = node.next

	def print_all_nodes_reverse(self):
		node = self.tail
		while node != None:
			print(node.value)
			node = node.prev


	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
			item.prev = None
			item.next = None
		else:
			self.tail.next = item
			item.prev = self.tail
		self.tail = item

	def find(self, value):
		node = self.head
		while node != None and self.compare(node.value, value) < 1:
			print(node.value)
			if node.value == value:
				return node
			node = node.next
		return None

	def get_at(self, index):
		node = self.head
		current = 0

		while node != None:
			if current == index:
				return node

			current += 1
			node = node.next
			
		return node

	def remove_by_value(self, value):
		node = self.head
		
		while node != None:
			if node.value == value:
				if node.prev == None:
					self.head = self.head.next
					return True
				else:
					node.prev.next = node.next
					return True

			node = node.next
		return False

	# Home work

	def compare(self, a, b):
		if self.sort_ascending:
			return a - b
		else:
			return b - a

	def insert(self, item):
		if self.head is None:
			self.head = item
			self.tail = item
			item.prev = None
			item.next = None
		else:
			node = self.head
			while node != None and self.compare(node.value, item.value) < 1:
				node = node.next


			if node != None:
				item.next = node
				item.prev = node.prev
				
				if node.prev != None:
					node.prev.next = item
				else:
					self.head = item
					item.prev = None

				node.prev = item
			else:
				self.tail.next = item
				item.prev = self.tail
				item.next = None
				self.tail = item


class StringOrderedList(OrderedList):
	
	def compare(self, a, b):

		stripedA = a.strip()
		strpedB = b.strip()

		if stripedA > strpedB:
			r = 1
		elif stripedA < strpedB:
			r = -1
		else:
			r = 0;
		
		if self.sort_ascending == False:
			r = -r

		return r
		
		
