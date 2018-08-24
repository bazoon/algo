class BinaryHeap():
	def __init__(self, n):
		self.tree = [None] * n
		self.current_index = 0
	
	def parent_index(self, index):
		return (index - 1) // 2


	def left_child_index(self, index):
		return 2 * index + 1

	def right_child_index(self, index):
		return 2 * index + 2

	def exchange(self, i, j):
		temp = self.tree[i]
		self.tree[i] = self.tree[j]
		self.tree[j] = temp

	def move_up(self, index):
		while self.parent_index(index) >= 0:
			if self.tree[self.parent_index(index)] < self.tree[index]:
				self.exchange(self.parent_index(index), index)
			index = self.parent_index(index)

	def add(self, value):
		self.tree[self.current_index] = value
		self.move_up(self.current_index)
		self.current_index += 1


	def remove(self):
		value = self.tree[0]
		self.tree[0] = self.tree[self.current_index - 1]
		self.tree[self.current_index - 1] = None
		self.current_index -= 1
		self.move_down(0)
		return value

	def move_down(self, index):
		while self.right_child_index(index) < len(self.tree):
			left_child = self.tree[self.left_child_index(index)]
			right_child = self.tree[self.right_child_index(index)]

			if right_child > left_child:
				if self.tree[index] < right_child:
					self.exchange(index, self.right_child_index(index))
					index = self.right_child_index(index)
				else:
					break
					
			else:
				if self.tree[index] < left_child:
					self.exchange(index, self.left_child_index(index))
					index = self.left_child_index(index)
				else:
					break		




# t = BinaryHeap(10)
# t.add(1)
# t.add(98)
# t.add(198)
# t.add(34)
# t.add(87)
# t.add(95)
# t.remove()


# print(t.tree)


