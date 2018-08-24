def is_equal(l):
	for i in range(len(l) - 1):
		if l[i] != l[i - 1]:
			return False

	return True
			

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

		
	values = list(count.values())
	if (is_equal(values)):
		return True

	m = max(values)
	m_index = values.index(m)
	values_copy = values.copy()
	values_copy[m_index] -=1

	if is_equal(values_copy):
		return True


	m = min(values)
	if m != 1:
		return False
	
	values.remove(m)

	return is_equal(values)
	
	
	


	

print(is_valid("xyyzzz"))	
		 
print(is_valid("xyz"))
print(is_valid("xxyyzzz"))
print(is_valid("xxyyz"))
print(is_valid("xyzzz"))
print(is_valid("xxyyzabc"))
