import math


def encode(s):
	chars = filter(lambda e: e != " ", list(s))
	l = len(chars)
	sq = math.sqrt(l)
	n_columns = int(math.ceil(sq))
	

	parts = [chars[i:i+n_columns] for i in range(0, l, n_columns)]
	
	result = ""
	for x in xrange(len(parts[0])):
		for z in xrange(len(parts)):
			pl = len(parts[z])
			if x < pl:
				result += parts[z][x]
		result += " "

	return result


def decode(p):
	result = ''
	lp = p.split(" ")
	for x in xrange(len(lp[0])):
		for z in lp:
			pl = len(z)
			if x < pl:
				result += z[x]
		

	return result


a = "hello world"
b = "This function is not accessible directly, so we need to import math module and then we need to call this function using math static object"


s = encode(a)
print s
print(decode(s))

