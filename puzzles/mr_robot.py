def is_sorted(a):
	for i in range(len(a) - 1):
		if a[i] > a[i+1]:
			return False
	return True


def is_three_sorted(a):
	return a[0] <= a[1] and a[1] <= a[2]

def rotate(a, start, end):
	temp = a[end]
	a[end] = a[end - 1]
	a[end - 1] = a[start]
	a[start] = temp
	return a

def can_be_sorted(a):
	l = len(a)

	for i in range(l - 2):
		for i in range(l - 2):
			j = 2
			while not is_sorted(a[i:i+3]) and j > 0:
				rotate(a, i, i + 2)
				j -= 1
			if not is_sorted(a[i:i+3]):
				return False


	return is_sorted(a)


a = [0, 1,3, 18,4,5,6,2,7, 18]


print(can_be_sorted(a))










