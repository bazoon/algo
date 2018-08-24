class TreeNode:
	def __init__(self, parent, value):
		self.parent = parent
		self.children = []
		self.value = value
		self.level = - 1

	def add(self, node):
		self.children.append(node)

class SimpleTree():
	def __init__(self, root):
		self.root = root
		
	def __iter__(self):
		return self

	def gen(self, node = None):
		yield(node)
		for n in node.children:
			for x in self.gen(n):
				yield x

	def __iter__(self):
	    return next(self)

	def next(self):
		for a in self.gen(self.root):
			yield(a)

	def remove(self, node):
		for child in node.children:
			child.parent = node.parent
			node.parent.add(child)

		node.parent.children.remove(node)

	def find_all(self, value):
		result = []
		for node in self.gen(self.root):
			if node.value == value:
				result.append(node)

		return result

	def move(self, node, to_node):
		node.parent.children.remove(node)
		to_node.add(node)

	def length(self):
		def aux(node):
			l = 0
			for n in node.children:
				l += 1 + aux(n)

			return l
		return aux(self.root)

	def set_level(self):
		def aux(node, level):
			node.level = level
			for child in node.children:
				aux(child, level + 1)
		
		aux(self.root, 1)



root = TreeNode(None, 0);
q = TreeNode(root, 1)
w = TreeNode(root, 2)

e = TreeNode(q, 3)
r = TreeNode(q, 4)
t = TreeNode(w, 5)
y = TreeNode(w, 6)

q.add(e)
q.add(r)
w.add(t)
w.add(y)

p = SimpleTree(root)
root.add(q)
root.add(w)


p.move(q, t)


print(p.length())
p.set_level()
for x in p:
	print(x.level)	


