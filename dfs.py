def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def move_left(a, i, step):
    max_index = len(a)

    while step > 0:
        while i >= 0  and i + step < max_index and a[i + step] < a[i]:
            exchange(a, i + step, i)
            i += step
        step -= 1


def sort_insert(a, step):
    for i, x in enumerate(a):
        move_left(a, i, step)

    print(a)


s = [7,6,5,4,3,2,1];

sort_insert(s, 3)