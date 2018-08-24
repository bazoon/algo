def add(s1, s2):
	l = max(len(s1), len(s2))
	

	result = []
	overflow = 0

	for index in range(l):
		c1i = len(s1) - index - 1
		c2i = len(s2) - index - 1


		if c1i >= 0:
			c1 = s1[c1i]
		else:
			c1 = 0

		if c2i >= 0:
			c2 = s2[c2i]
		else:
			c2 = 0


		c = int(c1) + int(c2) + overflow
		result.append(str(c % 10))
		if c >= 10:
			overflow = 1
		else:
			overflow = 0

	if overflow != 0:
		result.append(str(overflow))

	return "".join([i for i in reversed(result)])




def mul(s1, s2):
	
	times = min(len(s1), len(s2))


	if len(s1) > len(s2):
		times = int(s2)
		r = s1
		for x in range(times - 1):
			r = add(r, s1)
	else:
		times = int(s1)
		r = s2
		for x in range(times - 1):
			r = add(r, s2)


	return r

	
def fact(n):
	result = "1"
	for i in range(1, n + 1):
		
		result = mul(result, str(i))
	return result




print(fact(25))

# print(mul("123", "2000"))
# print(add("1107", "123"))
# multiply([1,2,3], 5)