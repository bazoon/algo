def has_dups(s):
	symbols = {}

	for c in s:
		if c in symbols:
			return True
		else:
			symbols[c] = True

	return False


print(has_dups("no dups!"))
print(has_dups("hello world"))
