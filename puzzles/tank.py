def list_to_s(l):
    lam = lambda x: str(x)
    return ''.join(map(lam, l))


def contains(l1, l2, start):
    l = lambda x: str(x)
    s1 = ''.join(map(l, l1))
    s2 = ''.join(map(l, l2))
    return s1.find(s2, start)


def check(a, b, left, right, top, bottom):
    r = 0
    c = 0

    for row in range(top, bottom + 1):
        c = 0
        for col in range(left, right + 1):
            if a[row][col] != b[r][c]:
                return False
            c += 1

        r += 1

    return True


def includes(map_arr, tank_arr):
    map_num_rows = len(map_arr)
    map_num_col = len(map_arr[0])

    tank_num_rows = len(tank_arr)
    tank_num_col = len(tank_arr[0])

    search_space = []

    for map_row in range(map_num_rows):
        for tank_row in range(tank_num_rows):
            m = map_arr[map_row]
            t = tank_arr[tank_row]

            index = contains(m, t, 0)
            indexes = []

            if index != -1:
                indexes.append(index)
                while True:
                    index = contains(m, t, index + 1)
                    if index == -1:
                        break
                    indexes.append(index)

            for index in indexes:
                left = index
                right = index + tank_num_col - 1
                top = map_row
                bottom = map_row + tank_num_rows - 1

                if right < map_num_col and bottom < map_num_rows:
                    search_space.append((left, right, top, bottom))

    

    return any([check(map_arr, tank_arr, x[0], x[1], x[2], x[3]) for x in search_space])



sample_map_1 = [
    [0, 2, 9, 4, 0, 2],
    [5, 6, 0, 2, 0, 2],
    [0, 2, 9, 6, 9, 4],
    [7, 8, 0, 2, 8, 8]
];

sample_tank_1 = [
    [0, 2],
    [9, 4],
    
]

sample_map_2 =[
    [3, 2, 1],
    [6, 9, 4],
    [7, 9, 8]
]

sample_tank_2 = [
    [6, 9],
    [9, 8]
]


sample_map_3 = [
    [9, 0, 0, 9, 3, 4, 3, 5, 2, 1 ,2, 6, 3, 6, 0],
    [1, 1, 9, 2, 1, 4, 1, 4, 4, 0 ,5, 8, 6, 5, 2],
    [9, 7, 9, 4, 8, 6, 0, 8, 2, 8 ,7, 5, 6, 9, 8],
    [3, 2, 2, 4, 3, 6, 5, 3, 1, 1 ,8, 5, 1, 6, 5],
    [8, 8, 7, 1, 0, 5, 9, 3, 0, 9 ,8, 7, 9, 5, 6],
    [2, 3, 2, 8, 0, 2, 6, 4, 4, 4 ,8, 8, 7, 8, 2],
    [3, 0, 2, 7, 7, 1, 9, 8, 9, 5 ,6, 6, 7, 9, 8],
    [0, 7, 3, 5, 7, 3, 2, 0, 7, 6 ,5, 4, 7, 8, 0],
    [3, 1, 1, 7, 5, 5, 7, 8, 5, 3 ,6, 2, 8, 0, 6],
    [9, 0, 9, 0, 0, 7, 9, 3, 9, 2 ,7, 2, 3, 0, 9],
    [3, 9, 5, 0, 9, 4, 8, 0, 5, 5 ,1, 6, 0, 8, 0],
    [5, 6, 2, 9, 1, 0, 8, 0, 5, 3 ,4, 9, 8, 1, 1],
    [9, 9, 3, 8, 5, 4, 3, 2, 4, 7 ,4, 4, 9, 7, 3],
    [7, 6, 8, 7, 0, 3, 4, 0, 4, 2 ,1, 9, 1, 9, 9],
    [6, 3, 0, 6, 2, 5, 2, 7, 0, 8 ,8, 7, 1, 9, 9],
]
sample_tank_3 = [
    [9, 9],
    [9, 9]
]

sample_map_4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

sample_tank_4 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
]


print("1", includes(sample_map_1, sample_tank_1))
print("2", includes(sample_map_2, sample_tank_2))
print("3", includes(sample_map_3, sample_tank_3))
print("4",includes(sample_map_4, sample_tank_4))
