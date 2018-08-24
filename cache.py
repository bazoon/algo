from random import randint

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


class Cache():
	def __init__(self, size = 17, step = 3):
		self.size = size
		self.step = step
		self.slots = [None] * size
		self.values = [None] * size
		self.hits = [0] * size

	def hash_fun(self, key):
		hash_value = hash(key) % self.size
		return hash_value

	def seek_slot(self, key):
		hash_value = self.hash_fun(key)
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
		else:
			index = self.find_most_unused_index()
			self.slots[index] = key
			self.values[index] = value
			self.hits[index] = 0
	
	def get(self, key):
		index = self.seek_slot(key)

		if index == None:
			return None

		self.hits[index] +=1	


		return self.values[index]

	def is_key(self, key):
		index = self.seek_slot(key)
		return self.slots[index] == key

	def find_most_unused_index(self):
		return self.hits.index(min(self.hits))

	


a = Cache(7, 2)

a.put("1", 1)
a.put("2", 2)
a.put("3", 3)
a.put("4", 4)
a.put("5", 5)
a.put("6", 6)
a.put("7", 7)



a.get("6")
a.get("3")
a.get("1")
print (a.hits)
a.put("8", 8)
print(a.slots) 


