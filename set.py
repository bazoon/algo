def c_mul(a, b):
    return eval(hex((long(a) * b) & 0xFFFFFFFFL)[:-1])

def hash(self):
    if not self:
        return 0 # empty
    value = ord(self[0]) << 7
    for char in self:
        value = c_mul(1000003, value) ^ ord(char)
    value = value ^ len(self)
    if value == -1:
        value = -2
    return value


class Powerset():
	def __init__(self, size = 17, step = 3):
		self.size = size
		self.step = step
		self.slots = [None] * size
		

	def hash_fun(self, value):
		hash_value = value % self.size
		return hash_value

	def seek_slot(self, value):
		hash_value = self.hash_fun(value)
		initial_hash_value = hash_value

		while self.slots[hash_value] != None and self.slots[hash_value] != value:
			hash_value = (hash_value + self.step) % self.size
			if hash_value == initial_hash_value:
				return None

		return hash_value
	
	def put(self, value):
		if self.is_key(value):
			pass
		index = self.seek_slot(value)

		if index != None:
			self.slots[index] = value
			
	
	def get(self, value):
		index = self.seek_slot(value)
		if index == None:
			return None
		return self.slots[value]


	def is_key(self, value):
		index = self.seek_slot(value)
		return self.slots[index] == value


	def remove(self, value):
		index = self.seek_slot(value)
		if index != None:
			self.slots[index] = None

	def intersection(self, other_set):
		result_set = Powerset()
		for value in self.slots:
			if value != None and other_set.is_key(value):
				result_set.put(value)
		return result_set

	def union(self, other_set):
		result_set = Powerset()
		for value in self.slots:
			if value != None:
				result_set.put(value)

		result_set.p()

		for value in other_set.slots:
			if value != None:
				result_set.put(value)

		return result_set

	def difference(self, other_set):
		result_set = Powerset()

		for value in self.slots:
			if value != None and not other_set.is_key(value):
				result_set.put(value)
		return result_set

	def is_subset(self, other_set):
		for value in other_set.slots:
			if value != None:
				if not self.is_key(value):
					return False

		return True

	def p(self):
		r = ""
		for value in self.slots:
			if value != None:
				r += str(value) + " "

		print r




