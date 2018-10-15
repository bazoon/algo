import sys

def kadane(a):
	l = len(a)
	max_ending_here = max_so_far = a[0]
	start = 0
	local_start = 0
	end = 0
	current_sum = 0
	result = -sys.maxsize - 1
	
	for i in range(l):
		x = a[i]

		current_sum += a[i]

		if current_sum < 0:
			current_sum = 0
			local_start = i + 1
		else:
			if current_sum > result:
				result = current_sum
				start = local_start
				end = i

	
	return [result, start, end]



def kadane2d(a):
	n_cols = len(a[0])
	n_rows = len(a)
	left = 0
	right = 0
	top = 0
	bottom = 0
	max_sum = -sys.maxsize - 1

	for left_col in range(n_cols):
		
		temp = [0] * n_rows

		for right_col in range(left_col, n_cols):
			
			for i in range(n_rows):
				temp[i] += a[i][right_col]

			[sum, t, b] = kadane(temp)

			if sum > max_sum:
				max_sum = sum
				left = left_col
				right = right_col
				top = t
				bottom = b
			

	print(max_sum, top, left, bottom, right)


a = [
	[-4, -2, -3, -4, -9],
	[-8, -3, 4,  2,  -1],
	[-3,  8, 10, 1,  -3],
	[-4, -1, -1, -7, -6]
]



kadane2d(a)
