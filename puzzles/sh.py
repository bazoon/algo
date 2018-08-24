def is_valid(p):
	l = list(p)
	count = {}
	
	max_count = 0
	min_count = -1
	max_key = None

	for x in l:
		if x in count:
			count[x] += 1
		else:
			count[x] = 1

	print(count)


	

	a = count['x']
	b = count['y']
	c = None
	
	if a == b:
		b = 0
	elif abs(a-b) > 1:
		return False
	else:
		if a != c or b !=c:
			return False


	return True


q=is_valid("xxyyzzz")

print(q)