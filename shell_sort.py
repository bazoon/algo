import random

def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def sort_insert(a):
    l = len(a)
    
    step = 1

    while step < len(a) / 3:
        step = 3 * step + 1

    while step > 0:
        i = step
        while i < l:
            j = i
            while  j > 0 and a[j] < a[j - step]:
                exchange(a, j, j - step)
                j -= step
                
            i += 1

        step /= 3
    
    print(a)


s = [];
for x in xrange(1,16):
    s.append(random.randint(1, 100))


sort_insert(s)