class Stack():
	"""docstring for Stack"""
	def __init__(self):
		self.stack = []

	def pop(self):
		if len(self.stack) == 0:
			return None
		return self.stack.pop()

	def push(self, value):
		return self.stack.append(value)

	def peak(self):
		if len(self.stack) == 0:
			return None
		return self.stack[-1]

	def size(self):
		return len(self.stack)


class OtherStack():
	def __init__(self):
		self.stack = []

	def push(self, value):
		self.stack.insert(0, value)
	
	def pop(self):
		if len(self.stack) == 0:
			return None

		v = self.stack[0];
		self.stack.remove(v)
		return v	

	def peak(self):
		if len(self.stack) == 0:
			return None
		return self.stack[0]

	def size(self):
		return len(self.stack)

def isBalanced(s):
	l = list(s)
	s = Stack()
	i = 0

	while i < len(l):
		v = l[i]
		if v == '(':
			s.push(v)
		else:
			w = s.pop()
			if (w != '('):
				return False

		i += 1

	return s.size() == 0



def eval_postfix(s):
	l = list(s)
	s1 = Stack()
	ops = {
		'+': lambda a, b: a + b,
		'-': lambda a, b: a - b,
		'*': lambda a, b: a * b,
		'/': lambda a, b: a / b
	}

	for i in reversed(l):
		if i!= " ":
			s1.push(i)
	
	s2 = Stack()

	while s1.size() != 0:
		v = s1.pop()
		
		if v in ["+", "-", "*", "/"]:
			a = s2.pop()
			b = s2.pop()
			s2.push(ops[v](int(a), int(b)))
		else:
			s2.push(v)

	r = s2.pop()
	if (r == '='):
		return s2.pop()

	


print(eval_postfix("8 2 + 5 * 9 + ="))
