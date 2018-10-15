import math


def master(doors):
    l = len(doors)

    # 1
    for i in range(l):
        doors[i] = True

    # 2
    for i in range(0, l, 2):
        doors[i] = False

    for s in range(3, l):
        for i in range(0, l, s):
            doors[i] = not doors[i]
            
        
    return doors


a = [False] * 1500


s = master(a)
l = len(s)
prev = -1

# for x in range(l):
#     if s[x]:
#         print(x)



def number_of_divs(n):
    
    count = 0
    for x in range(1, n + 1):
        if n % x == 0:
            count += 1

    return count




def foo():
    for x in range(1,1000):
        
        c = number_of_divs(x)
        if c % 2 != 0:
            print(x)




foo()

# print(number_of_divs(25))




