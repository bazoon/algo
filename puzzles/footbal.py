def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def is_sorted(a):
	l = len(a)
	for i in range(l - 1):
		if (a[i] > a[i + 1]):
			return False
	return True


def try_exchange(a):
	l = len(a)
	
	for i in range(l):
		j = l - i - 1

		if (a[i] > a[j]):
			exchange(a, i, j)
			return is_sorted(a)

		if i == j:
			break
	
	return False



def reverse_range(a, left, right):
	r = 0
	for i in range(left, right + 1):
		j = right - r
		if i >= j:
			break
		exchange(a, i, j)

		r += 1


def find_max_reverse_sorted_range(a, i):
	l = len(a) - 1 
	left = i
	right = i
	while i < l and a[i] > a[i + 1]: 
		i += 1
		right +=1

	return (left, right)

def try_reverse(a):
	l = len(a)

	diff = 0
	left = 0
	right = l - 1

	for i in range(l):
		
		(l, r) = find_max_reverse_sorted_range(a, i)
		
		if diff < abs(l - r):
			diff = abs(l - r)
			left = l
			right = r



	reverse_range(a, left, right)

	return is_sorted(a)
		
	
def try_sort(a):
	a1 = a.copy()

	return try_exchange(a) or try_reverse(a1)



print(try_sort([1, 3, 2]))
print(try_sort([3, 2, 1]))
print(try_sort([1, 7, 5, 3, 9]))
print(try_sort([9, 5, 3, 7, 1]))
print(try_sort([1, 4, 3, 2, 5]))

