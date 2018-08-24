class Deque():
	def __init__(self):
		self.queue = []

	def add_front(self, item):
		self.queue.append(item)

	def add_tail(self, item):
		self.insert(0, item)

	def remove_front(self):
		return self.queue.pop()

	def remove_tail(self):
		return self.queue.pop(0)

	def size(self):
		return len(self.queue)
		

def is_palindrome(s):
	if (len(s) == 1):
		return True

	l = list(s)
	dq = Deque()

	for x in l:
		dq.add_front(x)

	while dq.size() > 0:
		last = dq.remove_tail()
		
		if dq.size() > 0:
			first = dq.remove_front()
		else:
			return True
		
		if last != first:
			return False

	return True	


		






