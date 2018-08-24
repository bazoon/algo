class HashTable():
	def __init__(self, size, step):
		self.size = size
		self.step = step
		self.slots = [None] * size

	def hash_fun(self, value):
		hash_value = value % self.size
		initial_hash_value = hash_value

		while self.slots[hash_value] != None:
			hash_value = (hash_value + self.step) % self.size
			if hash_value == initial_hash_value:
				return None

		return hash_value

	def put(self, value):
		index = self.hash_fun(value)
		if index != None:
			self.slots[index] = value

	def find(self, value):
		return self.hash_fun(value)
			
	def p(self):
		print(self.slots)
	

h = HashTable(17, 3)
h.put(9)


print(h.find(9))
h.p()

