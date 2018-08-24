import ctypes
import unittest

class DynArray:

	def __init__(self):
		self.count = 0
		self.capacity = 16
		self.array = self.make_array(self.capacity)

	def __len__(self):
		return self.count

	def get_capacity(self):
		return self.capacity

	def make_array(self, new_capacity):
		return (new_capacity * ctypes.py_object)()

	def __getitem__(self, i):
		if i < 0 or i >= self.count:
			raise IndexError("Index out of bounds")
		return self.array[i]

	def  resize(self, new_capacity):
		new_array = self.make_array(new_capacity)
		for i in range(self.count):
			new_array[i] = self.array[i]

		self.array = new_array
		self.capacity = new_capacity

	def append(self, item):
		if self.count == self.capacity:
			self.resize(2 * self.capacity)
		self.array[self.count] = item
		self.count += 1

	def insert(self, index, item):
		if index < 0 or index >= self.count:
			raise IndexError("Index out of bounds")

		if self.count == self.capacity:
			self.resize(2 * self.capacity)

		for i in range(self.count - 1, index - 1, -1):
			self.array[i + 1] = self.array[i]
		self.array[index] = item

		self.count +=1

	# Alternative way
	def insert2(self, index, item):
		if index < 0 or index >= self.count:
			raise IndexError("Index out of bounds")

		if self.count == self.capacity:
			new_array = self.make_array(self.capacity * 2)
			for i in range (0, index):
				new_array[i] = self.array[i]
		else:
			new_array = self.array


		for i in range(self.count - 1, index - 1, -1):
			new_array[i + 1] = self.array[i]
		new_array[index] = item

		self.array = new_array
		self.count +=1

	def delete(self, index):
		if index < 0 or index >= self.count:
			raise IndexError("Index out of bounds")

		for i in range(index, self.count - 1):
			self.array[i] = self.array[i + 1]

		
		self.count -= 1

		if self.count * 2 <= self.capacity:
			new_capacity = max(16, self.capacity / 2)
			self.resize(new_capacity)

class MyTest(unittest.TestCase):

	def create_sample_array(self, i):
		da = DynArray()
		for i in range(i):
		    da.append(i)

		return da


	def test_insert(self):
		da = self.create_sample_array(16)
		self.assertEqual(da[0], 0)
		da.insert(0, 100)
		self.assertEqual(da[0], 100)
		self.assertEqual(da[1], 0)

		da = self.create_sample_array(16)
		self.assertEqual(da[6], 6)
		da.insert(6, 100)
		self.assertEqual(da[6], 100)
		self.assertEqual(da[7], 6)


		da = self.create_sample_array(16)
		self.assertEqual(da[15], 15)
		da.insert(15, 100)
		self.assertEqual(da[15], 100)
		self.assertEqual(da[16], 15)


	def test_delete(self):
		da = self.create_sample_array(16)

		self.assertEqual(da[0], 0)
		da.delete(0)
		self.assertNotEqual(da[0], 0)

		da = self.create_sample_array(16)
		self.assertEqual(da[5], 5)
		da.delete(5)
		self.assertNotEqual(da[5], 5)

		da = self.create_sample_array(16)
		self.assertEqual(da[15], 15)
		da.delete(15)
		self.assertRaises(IndexError, lambda: da[15])



		
unittest.main()





