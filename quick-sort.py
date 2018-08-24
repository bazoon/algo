import time
import random


# Function to generate
# and append them
# start = starting range,
# end = ending range
# num = number of
# elements needs to be appended
def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition(a, lo, hi):
    i = lo + 1
    j = hi
    N = a[lo]

    while True:
        while a[i] <= N and i <= j:
            i += 1
            
        while N <= a[j] and j >= i:
            j -= 1
            
        if (j < i):
            break;

        exchange(a, i, j)

    exchange(a, lo, j)
    return j



def quick_sort(a, left, right):
    if left >= right:
        return


    index = partition(a, left, right)

    quick_sort(a, left, index - 1)
    quick_sort(a, index + 1, right)


def divide(lst, pivot, start, end):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in xrange(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


a = [19, 4, 15, 12, 1, 3, 87, 7, 3, 5];
# a = [200, 300, 100, 400,130,900,1];


# a = rand(0, 20, 11)


# start = time.time()
# a = [4, 1, 4, 4, 9, 12, 12, 13, 16, 16, 17]
quick_sort(a, 0, len(a) - 1)
# partition(a,  0, len(a) - 1)
# divide(a, 4, 0, len(a) -1)
print(a)
# end = time.time()
# print("Quick sort time: " + str(end - start))


# start = time.time()
# sort_insert(a)
# end = time.time()
# print("Shell sort time: " + str(end - start))