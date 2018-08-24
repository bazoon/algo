import random
import string
import time

def string_index(value):
	return ord(value[0]) - ord('a')

def int_index(value):
	return int(value[1:])



def getOffset(value):
	return string_index(value) * 100 + int_index(value);

def add_digit(v):
		if v > 9:
			return str(v)
		else:
			return '0' + str(v)

def rand(num):
	res = []
	for j in range(num):
		res.append(random.choice(string.letters[0:26]) +  add_digit(random.randint(0, 99)))
	return res

def index_to_value(index):
	if index <= 99:
		return "a" + add_digit(int(str(index)))
	else:
		s = str(index)
		return chr(int(s[0]) + ord('a')) + add_digit(int(s[1:]))




def ksort(values):
	a = [0] * 26*100

	for v in values:
		offset = getOffset(v)
		a[offset] = 1 if a[offset] == 0 else a[offset] + 1

	r = []

	for i,x in enumerate(a):
		if i != 0:
			v = index_to_value(i)
			count = x
			while count > 0:
				r.append(v)
				count -= 1


	return r

start = time.time()
ksort(rand(10000000))
end = time.time()
print("Ksort time: " + str(end - start))



