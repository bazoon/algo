import random

def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


def calc(s, i, p):
	return s * ( 1 + i)**p



l = [(x, calc(x, 0.12, 10)) for x in rand(1, 100000, 20)]
		


for x in l:
	print(x)