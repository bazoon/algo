import random

def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition(a, lo, hi, cmp):
    i = lo + 1
    j = hi
    N = a[lo]

    while True:
        while i <= j and cmp(a[i], N) <= 0:
            i += 1
            
        while j >= i and cmp(N, a[j]) <= 0:
            j -= 1
            
        if (j < i):
            break;

        exchange(a, i, j)

    exchange(a, lo, j)
    return j



def quick_sort(a, left, right, cmp):
    if left >= right:
        return


    index = partition(a, left, right, cmp)

    quick_sort(a, left, index - 1, cmp)
    quick_sort(a, index + 1, right, cmp)


def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


def array_to_start_impulse(a):
    l = len(a)
    middle_index = l // 2
    asc = lambda a, b: a - b
    desc = lambda a, b: b - a
    quick_sort(a, 0, len(a) - 1, asc)
    [rest, max_element] = a[0:-1], a[-1]
    rest.insert(middle_index, max_element)
    quick_sort(rest, middle_index, len(a) - 1, desc)
    return rest


def array_to_start_impulse2(a):
    sorted_a = sorted(a)
    l = len(a)
    middle_index = l // 2
    result = [i for i in sorted_a[0:middle_index]]
    result.append(max(a))
    return result + [i for i in reversed(sorted_a[middle_index+1:-1])]

def array_to_start_impulse3(a):
    sorted_a = sorted(a)
    l = len(a)
    middle_index = l // 2
    return sorted_a[0:middle_index] + [i for i in reversed(sorted_a[middle_index+1:-1])]


def check(a):
    l = len(a)
    middle_index = l // 2
    return all(a[i] <= a[i+1] for i in xrange(middle_index-1)) and all(a[i] >= a[i + 1] for i in xrange(middle_index + 1, l - 1)) and a[middle_index] == max(a)



def test():
    res = []
    for x in xrange(1, 100):
        a = rand(1, 100, 999)
        res.append(check(array_to_start_impulse(a)))
    return all(res)



a = rand(1, 100, 25)


# s = sorted(a)
# print(s)
i = array_to_start_impulse3(a)
print(i)
# print(check(i))
# print(test())
# asc = lambda a, b: a - b
# desc = lambda a, b: b - a
# quick_sort(a, 0, len(a) - 1, desc)
# print(a)




