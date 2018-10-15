import random
import time

def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


def twice(f, a):
	return f(f(a))

def trans(a):
	l = len(a)
	b = []

	for i in range(l):
		for j in range(l - i):
			k = i + j

			m = max(a[j:(k+1)])
			

			b.append(m)


	return b

def key(a):
	b = twice(trans, a)
	return sum(b)

def avg(l):
    s = 0
    for x in l:
        s += x
    return s / len(l)


def run(f, msg, start, end, size, number_of_trials = 1):
    results = []
    for x in range(number_of_trials):
        t0 = time.time()
        b = rand(start, end, size)
        f(b)
        t1 = time.time()
        results.append(t1 - t0)

        print("msg: " + msg + " average time:  " + str(avg(results)))


K = 20
lg = [0]*(1 << K)

def make_rangemax(A):
    n = len(A)
    assert 1 << K > n

    key = lambda x: A[x]
    mxk = []
    mxk.append(range(n))
    for k in xrange(K-1):
        mxk.append(list(mxk[-1]))
        for i in xrange(n - (1 << k)):
            mxk[k+1][i] = max(mxk[k][i], mxk[k][i + (1 << k)], key=key)
    def rangemax(i, j):
        k = lg[j - i]
        return max(mxk[k][i], mxk[k][j - (1 << k)], key=key)
    return rangemax


def brutesolo(A):
    rangemax = make_rangemax(A)
    stack = [(0, len(A))]
    ans = 0
    while stack:
        i, j = stack.pop()
        if i != j:
            x = rangemax(i, j)
            stack.append((i, x))
            stack.append((x + 1, j))
            ans += A[x] * (x - i + 1) * (j - x)
    return ans

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


def nln(a):
	stack = Stack()
	l = len(a)
	lnln = [0] * l

	for i in range(l):
		while stack.size() > 0 and a[i] > a[stack.peak()]:
			stack.pop()

		if stack.size() == 0:
			lnln[i] = -20
		else:
			lnln[i] = stack.peak()

		stack.push(i)

	return lnln

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [3, 5, 4, 1, 2]

# print(nln(c))
# print(trans(c))


# print(make_rangemax(c)(0,5))

# for x in xrange(0, 80, 10):
# 	run(key, str(x), 0, 100, x)


# print(brutesolo(c))
# print(sum(twice(trans, c)))
