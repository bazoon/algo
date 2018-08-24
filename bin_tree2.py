class Tree():
	def __init__(self, n):
		self.tree = [None] * n
	

	def left_child_index(self, index):
		return 2 * index + 1

	def right_child_index(self, index):
		return 2 * index + 2

	def find(self, value):
		def aux(index):
			if index >= len(self.tree) - 1:
				return None

			if self.tree[index] == value or self.tree[index] is None:
				return -index
			elif self.tree[index] > value:
				return aux(self.right_child_index(index))
			else:
				return aux(self.left_child_index(index))

		return aux(0)

	def add(self, value):
		index_to_insert = self.find(value)
		if index_to_insert is None:
			return


		if index_to_insert <= 0:
			self.tree[-index_to_insert] = value


t = Tree(10)


t.add(100)
t.add(200)
t.add(90)
t.add(220)
t.add(120)
t.add(95)
t.add(89)

print(t.tree) #[100, 200, 90, 220, 120, 95, 89, None, None, None]

	  #        100
	  #    200     90
	  # 220  120 95  89
	   



