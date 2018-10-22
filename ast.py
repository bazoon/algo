from random import random, randint, choice


def randomExp(n):
	ops = ["+", "-", "*", "/"]
	r = ""
	for x in range(n):
		op = choice(ops)
		left = randint(1, 9)
		right = randint(1, 9)
		r = r + str(left) + " " + op + " " + str(right)
	return r

class ANode():
	def __init__(self,token_type, token_value):
		self.token_type = token_type
		self.token_value = token_value
	def __str__(self):
		return '[ ' + self.token_type +', ' + self.token_value +' ]'


class TreeNode:
	def __init__(self, parent, value):
		self.parent = parent
		self.left = None
		self.right = None
		self.value = value
		self.level = - 1

	def addLeft(self, node):
		self.left = node
		return node

	def addRight(self, node):
		self.right = node
		return node

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

	



subs = {
	'/': '!',
	'*': '@',
	'+': '$',
	'-': '%'
}

reverse_subs = {
	'!': '/',
	'@': '*',
	'$': '+',
	'%': '-'
}

def decode(s):
	l = s[0].split(' ')
	return [reverse_subs.get(x, x) for x in l]

def place_brackets(s, op):
	if op in s:
		op_index = s.index(op)
	else:
		return s
	
	left = s[op_index - 1]
	right = s[op_index + 1]
	rest = s[op_index + 2:]
	prev = s[:op_index - 1]
	
	ns = prev + ['(' +' ' + left +' '+ subs[op] +' ' + right+ ' )'] + rest
	return place_brackets(ns, op)


def tokenize(exp):
	next_exp = place_brackets(exp.split(), '/')
	next_exp = place_brackets(next_exp, '*')
	next_exp = place_brackets(next_exp, '-')
	next_exp = place_brackets(next_exp, '+')
	return decode(next_exp)


def to_node(token):
	if token == '(' or token == ')':
		return ANode("bracket", token)
	elif token in ['/', '*', '+', '-']:
		return ANode("operation", token)
	else:
		return ANode("number", token)

def to_nodes(tokens):
	return map(lambda t: to_node(t), tokens)


def is_op(token):
	return token in ['/', '*', '-', '+']

def to_ast(tokens):
	node = TreeNode(0, None)
	tree = SimpleTree(node)
	l = len(tokens)


	for i in range(l):
		t = tokens[i]

		if (t == '('):
			node = node.addLeft(TreeNode(node, None))
		elif (t == ')'):
			node = node.parent
		elif (t in ['/', '*', '-', '+']):
			node.value = t
			node = node.addRight(TreeNode(node, None))
		else:
			node.value = t
			node = node.parent

	return tree

def print_tree(t, pad=" "):
	
	if t != None:
		print(pad+t.value)


	if (t.left != None):
		print_tree(t.left, " " * (len(pad)+1))

	if (t.right != None):
		print_tree(t.right, " " * (len(pad)+1))

def eval_op(op, left, right):
	a = float(left)
	b = float(right)

	if op == '+':
		return a + b
	elif op == '-':
		return a - b
	elif op == '*':
		return a * b
	elif op == '/':
		return a /b



def eval_ast(ast):
	if (is_op(ast.value)):
		left_result = eval_ast(ast.left)
		right_result = eval_ast(ast.right)
		ast.result = eval_op(ast.value, left_result, right_result)
		ast.trans = '(' + ast.left.trans + ast.value + ast.right.trans + ')'
		return ast.result
	else:
		ast.result = int(ast.value)
		ast.trans = ast.value
		return ast.result


exp = "20 / 4 + 5 * 7 - 20 + 9 * 7"


# print(ast.root.trans)
# print_tree(ast.root)
# print(randomExp(10))


for x in range(100):
	exp = randomExp(20)
	tokens = tokenize(exp)
	ast = to_ast(tokens)
	eval_ast(ast.root)
	ast_result = ast.root.result
	eval_result = eval(exp)
	d = abs(ast_result) - abs(eval_result)

	print(exp)
	print("Result from AST", ast_result, "Result from Eval", eval_result, "Diff: ", d)
	
	


