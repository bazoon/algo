class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

	

class LinkedList:  
	def __init__(self):
		self.head = None
		self.tail = None

	def add_in_tail(self, item):
		if self.tail is None:
			self.head = item
		else:
			self.tail.next = item
		self.tail = item

	def print_all_nodes(self):
		node = self.head
		while node != None:
			print(node.value)
			node = node.next

	def find(self, value):
		node = self.head
		while node != None:
			if node.value == value:
				return node
			node = node.next
		return None

	
	def remove_by_value(self, value):
		node = self.head
		prior = None

		while node != None:
			if node.value == value:
				if prior == None:
					self.head = self.head.next
					return True
				else:
					prior.next = node.next
					return True

			prior = node
			node = node.next
		return False

	def remove_all_by_value(self, value):
		node = self.head
		prior = None

		while node != None:
			if node.value == value:
				if prior == None:
					self.head = self.head.next
				else:
					prior.next = node.next

			prior = node
			node = node.next
	
	def clear(self):
		self.head = None
		self.tail = None

	def find_all(self, value):
		node = self.head
		found_items = []

		while node != None:
			if node.value == value:
				found_items.append(node)
			node = node.next
		return found_items


	def length(self):
		node = self.head
		length = 0
		while node != None:
			length += 1
			node = node.next

		return length

	def insert_after(self, after_node, n):
		node = self.head
		
		while node != None:
			if node == after_node:
				n.next = node.next
				node.next = n
				return
			node = node.next


def add_list_values(list1, list2):

	node1 = list1.head
	node2 = list2.head
	result_list = LinkedList()

	while node1 != None or node2 != None:

		if (node1 == None or node2 == None):
			return None

		result_list.add_in_tail(Node(node1.value + node2.value))
		node1 = node1.next
		node2 = node2.next

	return result_list


