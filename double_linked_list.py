import unittest

class Node2:
	def __init__(self, v):
		self.value = v
		self.prev = None
		self.next = None

class LinkedList2:
	def __init__(self):
		self.head = None
		self.tail = None

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
		while node != None:
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

	
	# Homework

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

	def insert_after(self, after_node, n):
		node = self.head
		
		while node != None:
			if node == after_node:
				
				n.next = node.next
				if n.next != None:
					n.next.prev = n
				else:
					self.tail = n

				node.next = n
				n.prev = node
				return True
			node = node.next

	def insert_to_head(self, node):
		node.next = self.head
		if self.head:
			self.head.prev = node
		self.head = node
		node.prev = None



def create_sample_list(i):
	list = LinkedList2()

	for x in xrange(1, i):
		node = Node2(i)
		list.add_in_tail(node)

	return list


class MyTest(unittest.TestCase):

	def create_sample_list(self, i):
		list = LinkedList2()

		for x in range(1, i):
			list.add_in_tail(Node2(x))

		

		return list


	def test_remove_by_value(self):
		list = self.create_sample_list(10)
		node = list.find(4)
		
		self.assertEqual(list.find(1).value, 1)
		self.assertEqual(list.find(5).value, 5)
		self.assertEqual(list.find(9).value, 9)
		
		list.remove_by_value(1)
		self.assertIsNone(list.find(1))

		list.remove_by_value(5)
		self.assertIsNone(list.find(5))

		list.remove_by_value(9)
		self.assertIsNone(list.find(9))


	def test_insert_after(self):
		list = self.create_sample_list(10)

		#after first
		node = list.get_at(0)

		self.assertEqual(list.get_at(0).value, 1)
		self.assertEqual(list.get_at(1).value, 2)
		self.assertEqual(list.get_at(2).value, 3)


		list.insert_after(node, Node2(11))

		self.assertEqual(list.get_at(0).value, 1)
		self.assertEqual(list.get_at(1).value, 11)
		self.assertEqual(list.get_at(2).value, 2)


		# #in the middle
		list = self.create_sample_list(10)
		node = list.get_at(5)

		self.assertEqual(list.get_at(5).value, 6)
		self.assertEqual(list.get_at(6).value, 7)
		self.assertEqual(list.get_at(7).value, 8)


		list.insert_after(node, Node2(11))

		self.assertEqual(list.get_at(5).value, 6)
		self.assertEqual(list.get_at(6).value, 11)
		self.assertEqual(list.get_at(7).value, 7)

		
		#in the end

		list = self.create_sample_list(10)
		node = list.get_at(8)

		self.assertEqual(list.get_at(8).value, 9)
		self.assertIsNone(list.get_at(9))
		

		list.insert_after(node, Node2(11))

		self.assertEqual(list.get_at(8).value, 9)
		self.assertEqual(list.get_at(9).value, 11)
		self.assertIsNone(list.get_at(10))

	def test_insert_to_head(self):
		list = self.create_sample_list(5)

		first = list.head
		second = list.head.next
		third = list.head.next.next

		node = Node2(11)

		list.insert_to_head(node)

		self.assertEqual(list.head, node)
		self.assertIsNone(node.prev)
		self.assertEqual(node.next, first)
		self.assertEqual(first.prev, node)


unittest.main()
