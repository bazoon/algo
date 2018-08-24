# -*- coding: utf-8 -*-
from itertools import permutations


def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition(a, lo, hi):
    i = lo + 1
    j = hi
    N = a[lo]

    while True:
        while i <= j and a[i] <= N:
            i += 1

        while j >= i and N <= a[j]:
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


def exchange(s, i, j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    return ''.join(s)


def find(s):
    two = [''.join(i) for i in permutations(s)]

    larger = []

    for f in two:

        if f > s:
            larger.append(f)

    return sorted(larger)[0]


def find_less(s):
    start_index = len(s) - 1
    search_range = reversed(range(0, start_index))

    for index in search_range:
        if s[index] < s[index + 1]:
            return index

    return -1


def find_greater(s, start_index):
    search_range = reversed(range(start_index + 1, len(s)))
    for index in search_range:

        if s[index] > s[start_index]:
            return index

    return -1


def magic(s):
    l = len(s) - 1;
    ls = list(s)
    initial_word = s
    results = []
    
    while True:
        i = find_less(ls)
        
        if i == -1:
            if len(results) > 0:
                return min(results)
            else:
                return -1

        if i < l:
            j = find_greater(ls, i)
            print(i, j, ls[i], ls[j])
            exchange(ls, i, j)
        quick_sort(ls, i + 1, l)
        

        current_word = ''.join(ls)
        print(current_word)
        if current_word > initial_word:
            results.append(current_word)
        elif current_word == initial_word:
            return -1




# "ая" преобразовываем в "яа"
# "fff" - невозможно преобразовать
# "нклм" в "нкмл"
# "вибк" в "викб"
# "вкиб" в "ибвк"

cases = ["ая", "fff", "нклм", "вибк", "вкиб"]

# [print(magic(i)) for i in cases]
magic("вкиб")