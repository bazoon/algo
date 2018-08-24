class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)


	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def rotate(self, n):
		while n > 0:
			self.enqueue(self.dequeue())
			n -= 1


class Stack():
	"""docstring for Stack"""
	def __init__(self):
		self.stack = []

	def pop(self):
		if len(self.stack) == 0:
			return None
		return self.stack.pop()

	def push(self, value):
		return self.stack.append(value)

	def peak(self):
		if len(self.stack) == 0:
			return None
		return self.stack[-1]

	def size(self):
		return len(self.stack)

class CustomQueue:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def enqueue(self, item):
		self.stack1.push(item)

	def dequeue(self):
		while self.stack1.size() > 0:
			self.stack2.push(self.stack1.pop())

		return self.stack2.pop()

	def size(self):
		return self.stack1.size() + self.stack2.size()


