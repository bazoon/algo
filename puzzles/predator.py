import random

def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


def find_dups(l):
	bits = [0] * 4096

	for i in l:
		bit_position = i / 8;
		index_in_byte = i % 8
		bit = bits[bit_position]

		test_mask = 1 << index_in_byte

		if (bits[bit_position] & test_mask == test_mask):
			print(i)
		else:
			bits[bit_position] |= 1 << index_in_byte 




a = [32, 12, 32, 12, 1, 2, 3, 4, 5, 1]			
# a = rand(0, 32000, 10000)
find_dups(a)

