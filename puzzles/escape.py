import random
import time
import math

class Stack():
    """docstring for Stack"""
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)





def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


# Brute force 1 day
def escape(list):
    length = len(list)

    to_delete = []

    for i in range(length - 1):
        if (list[i + 1] > list[i]):
            to_delete.append(i + 1)

    new_list = []
    for x in range(length):

        if not x in to_delete:
            new_list.append(list[x])

    return new_list


# Brute force version
def count_escapes(list, should_print = False):
    n = 0
    new_list = list
    while True:
        length = len(new_list)
        new_list = escape(new_list)
        new_len = len(new_list)

        if new_len == length:
            break

        if should_print:
            print(new_list)
        n += 1

    return n


def find_initial_indexes(list):
    l = len(list)
    in_list = [i for i in range(l)]
    to_remove = []

    for i in range(l - 1):
        if list[i] < list[i + 1]:
            to_remove.append(i + 1)

    return [set(in_list), set(to_remove)]


def find_indexes(list, idx, in_list):
    l = len(list)

    if idx < 0 or idx >= l - 1:
        return [-1, -1]

    left_idx = idx - 1
    right_idx = idx + 1

    while left_idx > 0 and not left_idx in in_list:
        left_idx -= 1

    while right_idx < l and not right_idx in in_list:
        right_idx += 1

    if left_idx >= 0 and right_idx < l and list[left_idx] < list[right_idx]:
        return [left_idx, right_idx]

    return [-1, -1]


# Home work
def escape4(list):
    [in_list, to_remove] = find_initial_indexes(list)

    next_remove = set()
    count = 0

    while len(to_remove) > 0:

        in_list.difference_update(to_remove)

        # print(in_list)
        next_remove.clear()

        for idx in to_remove:
            [left_idx, right_idx] = find_indexes(list, idx, in_list)
            if left_idx != -1 and right_idx != -1:
                next_remove.add(right_idx)

        to_remove.clear()
        to_remove.update(next_remove)

        count += 1

    return count


def left(l):
    length = len(l)
    r = []

    r.append(l[0])

    for i in range(1, length):
        current = l[i]
        top = r.pop()

        if current > top:
            r.append(top)
        else:
            r.append(top)
            r.append(current)

    return r


def escape5(l):
    length = len(l)

    r = Stack()
    days = 0

    last = left(l)

    for i in range(0, length):

        current = l[i]

        if r.size() == 0:
            r.push((current, 0))
        else:
            (top, day) = r.top()

            if current > top:
                days = max(days, 1)
                r.push((current, 1))
            else:
                v = r.top()
                pr = v[1]

                while r.size() > 0 and v[0] >= current:
                    r.pop()

                    if r.size() == 0:
                        break

                    pr = max(pr, v[1])
                    v = r.top()

                if r.size() == 0:
                    r.push((current, 0))
                else:
                    r.push((current, pr + 1))
                    days = max(days, pr + 1)


        
    return days


def accuracy(f, start, end, size):
    right = 0;
    wrong = 0
    for l in range(100):
        b = rand(start, end, size)
        if (count_escapes(b) - f(b)) <= 0:
            right += 1
        else:
            print(b)
            wrong += 1

    
    return (right / (right + wrong))


def avg(l):
    s = 0
    for x in l:
        s += x
    return s / len(l)

def std(l):
    av = avg(l)
    diffs = [(x - av)*(x - av) for x in l]
    return math.sqrt(avg(diffs))

def run(f, msg, start, end, size, number_of_trials = 1):
    results = []
    for x in range(number_of_trials):
        t0 = time.time()
        b = rand(start, end, size)
        f(b)
        t1 = time.time()
        results.append(t1 - t0)

    print("msg: " + msg + " average time:  " + str(avg(results))+ " standard deviation: " + str(std(results)))



# run(count_escapes, "N*N", 1, 1000, 30000, 10)
run(escape4, "N*LogN", 1, 1000, 50000, 10)
run(escape5, "N", 1, 1000, 50000, 10)


print(accuracy(escape4, 1, 100, 1000))
print(accuracy(escape5, 1, 100, 1000))

