import random

def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


def reverse(a, i):
    length = len(a)

    j = length - 1

    while i <= j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        j -= 1
        i += 1


def make_first(a, from_index, to_index):
    reverse(a, from_index)
    reverse(a, to_index)


def is_sorted(l):
    length = len(l)

    for i in range(length - 1):
        if (l[i] < l[i + 1]):
            return False

    return True


def hack(l, current):
    if current == len(l) - 1:
        return

    m = l[current]
    max_index = current
    for j in range(current, len(l)):
        if m < l[j]:
            m = l[j]
            max_index = j

    
    make_first(l, max_index, current)
    hack(l, current + 1)


a = [20, 1, 4, 10, 2, 7, 9, 2]
a = rand(0, 1000, 200)
# a = [100, 21, 12, 86, 27, 90, 76, 97, 97, 72, 70, 63, 62, 58, 52, 42, 20, 17, 9, 5]
hack(a, 0)

# make_first(a, 3, 1)
# reverse(a, 2)
print(a)