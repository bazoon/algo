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



def is_balanced(l):
	s = Stack()
	length = len(l)

	for bracket in l:
		if bracket == '(':
			s.push(bracket)
		else:
			if s.size() > 0:
				matching_bracket = s.pop()
				if matching_bracket == ')':
					return False

			else:
				return False

	return s.size() == 0

def permutation(xs):
    if len(xs) == 1:
        return [xs]
    ret = []
    for x in xs:
    	ys = xs[:]
    	ys.remove(x)
        for y in permutation(ys):
            ret.append([x] + y)
    return ret        

def ring(n):
	l = []
	for x in range(n):
		l.append('(')
		l.append(')')

	all_possible = permutation(l)

	return set(["".join(x) for x in all_possible if is_balanced(x)])


# print(permutation(['(',')','(', ')']))
# print(ring(4))


def print_balanced(n):
	s = [None] * 2 * n
	print_balanced_aux(s, 0, n, 0, 0)




def print_balanced_aux(s, position, n, open_count, close_count):
	
	if close_count == n:
		print(s)
		return
	else:
		if open_count > close_count:
			s[position] = ")"
			print_balanced_aux(s, position + 1, n, open_count, close_count + 1)
		
		if open_count < n:
			s[position] = "("
			print_balanced_aux(s, position + 1, n, open_count + 1, close_count)



print_balanced(2)
