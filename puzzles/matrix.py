import random


def random_matrix(rows, cols):
	n_rows = random.randint(1, rows)
	n_cols = random.randint(1, cols)


	if n_rows < n_cols and n_rows % 2 != 0:
		n_rows +=1
	elif n_cols < n_rows and n_cols % 2 != 0:
		n_cols += 1

	return [[random.randint(11, 99) for x in range(n_rows)] for n in range(n_cols)]



def print_matrix(m):
	for x in m:
		print(x)
	print("")

def clone_matrix(m):
	return [[0 for x in range(len(m[0]))] for n in m]


def rotate_rim(m, rows_start, columns_start, n_rows, n_cols, out_m):
	i = columns_start
	j = rows_start

	i_dir = 1
	j_dir = 0

	while True:
		elem = m[j][i]
		# print(elem)


		i += i_dir
		j += j_dir

		out_m[j][i] = elem

		if i == n_cols - 1 and j < n_rows - 1:
			i_dir = 0
			j_dir = 1
		
		if i == n_cols - 1 and j == n_rows - 1:
			i_dir = -1
			j_dir = 0
		
		if i == columns_start and j == n_rows - 1:
			i_dir = 0
			j_dir = -1
		if i == columns_start and j == rows_start:
			break


def rotate_matrix_once(m):
	n_rows = len(m)
	n_cols = len(m[0])

	n_rims = min(n_rows, n_cols) // 2
	
	rows_start = 0
	columns_start = 0
	out_matrix = clone_matrix(m)

	for x in range(n_rims):
		rotate_rim(m, rows_start, columns_start, n_rows, n_cols, out_matrix)
		rows_start += 1
		columns_start += 1
		n_rows -= 1
		n_cols -= 1

	return out_matrix


def rotate_matrix(m, times):
	out_m = m
	for x in range(times):
		out_m = rotate_matrix_once(out_m)

	return out_m

matrix = [
	[1, 2, 3, 4, 5, 6],
	[2, 3, 4, 5, 6, 7],
	[3, 4, 5, 6, 7, 8],
	[4, 5, 6, 7, 8, 9],
]

matrix0 = [
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
]

r= [[84, 81, 88, 18, 43, 16, 68, 77],
    [22, 75, 17, 26, 82, 83, 41, 12],
    [15, 72, 35, 83, 80, 35, 91, 52],
    [57, 81, 31, 28, 98, 30, 62, 36],
    [21, 42, 65, 70, 20, 35, 92, 83],
    [77, 39, 22, 87, 61, 12, 18, 99],
    [92, 50, 18, 60, 48, 87, 30, 58],
    [57, 62, 75, 24, 62, 56, 15, 58]]

r1 = [[40, 87, 33, 19, 17],
	  [85, 62, 49, 23, 83],
	  [72, 89, 64, 70, 32],
	  [60, 56, 79, 36, 36]]

# rotate_rim(matrix, 0, 0, len(matrix), len(matrix[0]), matrix0)
# rotate_rim(matrix, 1, 1, len(matrix) - 1, len(matrix[0]) - 1, matrix0)

# print_matrix(matrix)



# print_matrix(rm)

r_matrix = random_matrix(5, 5)
# print_matrix(r_matrix)
# r_matrix = matrix
print_matrix(r_matrix)
rtm = rotate_matrix(r_matrix, 3)
print_matrix(rtm)