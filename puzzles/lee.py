import random


def gen2():
	return random.choice([0,1])

def gen3():
	a = str(gen2()) + str(gen2())

	if a == "00":
		return 0
	if a == "01":
		return 1
	if a == "10":
		return 2

	return gen3()


		

def count(a, n):
	return len([x for x in a if x == n]) / len(a)


a = [gen3() for i in range(100000)]
print(count(a, 0))
print(count(a, 1))
print(count(a, 2))
print("")

