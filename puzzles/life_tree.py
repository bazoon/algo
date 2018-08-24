import random

def random_tree(num_rows, num_columns):
	return [[random.choice([".","+"]) for i in range(num_columns)] for row in range(num_rows)]

def print_tree(tree):
	num_rows = len(tree)
	num_columns = len(tree[0])

	for row in range(num_rows):
		s = ""
		for column in range(num_columns):
			cell = tree[row][column]
			s += str(cell) + " "

		print(s)

	print("")


def destroy(tree):
	num_rows = len(tree)
	num_columns = len(tree[0])

	to_destroy = [[None for i in range(num_columns)] for row in range(num_rows)]
	
	for row in range(num_rows):
		for column in range(num_columns):
			cell = tree[row][column]

			if cell >= 3:
				top = row - 1
				bottom = row + 1
				left = column - 1
				right = column + 1

				if top >= 0:
					to_destroy[top][column] = True
				if bottom <= num_rows - 1:
					to_destroy[bottom][column] = True
				if left >= 0:
					to_destroy[row][left] = True
				if right <= num_columns - 1:
					to_destroy[row][right] = True
				to_destroy[row][column] = True

	for row in range(num_rows):
		for column in range(num_columns):
			if to_destroy[row][column]:
				tree[row][column] = "."


	return tree
	
def prepare(tree):
	num_rows = len(tree)
	num_columns = len(tree[0])

	for row in range(num_rows):
		for column in range(num_columns):
			if tree[row][column] == "+":
				tree[row][column] = 1	
			
	return tree

def evolve(tree):
	num_rows = len(tree)
	num_columns = len(tree[0])

	tree = prepare(tree)

	for row in range(num_rows):
		for column in range(num_columns):
			if tree[row][column] == ".":
				tree[row][column] = 1
			else:
				tree[row][column] += 1	
	return tree

def step(tree):
	num_rows = len(tree)
	num_columns = len(tree[0])
	print(num_rows, num_columns)



def sim(tree, n):
	
	for year in range(n):
		tree = evolve(tree)

		if year % 2 == 1:
			tree = destroy(tree)

	return tree




example_tree = [
	[".", ".", ".", ".", ".", ".", "."],
	[".", ".", ".", "+", ".", ".", "."],
	[".", ".", ".", ".", "+", ".", "."],
	[".", ".", ".", ".", ".", ".", "."],
	["+", "+", ".", ".", ".", ".", "."],
	["+", "+", ".", ".", ".", ".", "."]
]

print_tree(sim(example_tree, 25))



r_tree = random_tree(10,10)
print_tree(sim(r_tree, 42))
