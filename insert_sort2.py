def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def sort_insert(a, step):
    l = len(a)

    while step > 0:
        i = step
        while i < l:
            j = i
            while  j > 0 and a[j] < a[j - step]:
                exchange(a, j, j - step)
                j -= step
                
            i += 1

        step -= 1
    
    print(a)


s = [7,6,5,4,3,2,1];

sort_insert(s, 1)