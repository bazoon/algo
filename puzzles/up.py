def find_place(prizes, n):
	d = {}
	place = 1
	places = []

	for x in prizes:
		if d.get(x) == None:
			d[x] = 1
			places.append(x)

	place = 1
	for p in places:
		if n >= p:
			break
		place += 1


	return place

def up(prizes, bad_r_prizes):
	ups = []
	p = 0

	for x in bad_r_prizes:
		p += x
		ups.append(find_place(prizes, p))

	return ups

print(up([100,100, 99,99,99, 95,95, 90,90, 1,1,1], [0,1,89,4,5,1,1,1]))

