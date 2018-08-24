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


class HashTable():
	def __init__(self, size = 17, step = 3):
		self.size = size
		self.step = step
		self.slots = [None] * size
		self.values = [None] * size


	def hash_fun(self, key):
		hash_value = hash(key) % self.size
		return hash_value

	def seek_slot(self, key):
		hash_value = self.hash_fun(key)
		print(key, hash_value)
		initial_hash_value = hash_value

		while self.slots[hash_value] != None and self.slots[hash_value] != key:
			hash_value = (hash_value + self.step) % self.size
			if hash_value == initial_hash_value:
				return None

		return hash_value

	
	def put(self, key, value):
		index = self.seek_slot(key)

		if index != None:
			self.slots[index] = key
			self.values[index] = value

	
	def get(self, key):
		index = self.seek_slot(key)
		if index == None:
			return None
		return self.values[index]


	def is_key(self, key):
		index = self.seek_slot(key)
		return self.slots[index] == key


	