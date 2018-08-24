import heapq
import random


# helper stuff

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0


def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


class MaxHeapObj(object):
    def __init__(self, val): self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)


class MinHeap(object):
    def __init__(self): self.h = []

    def heappush(self, x): heapq.heappush(self.h, x)

    def heappop(self): return heapq.heappop(self.h)

    def __getitem__(self, i): return self.h[i]

    def __len__(self): return len(self.h)


class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self): return heapq.heappop(self.h).val

    def __getitem__(self, i): return self.h[i].val


# Home work

class ListWithMedian():
    def __init__(self):
        self.l = []
        self.length = 0
        self.before = MaxHeap()
        self.after = MinHeap()
        self.median = None

    def insert(self, v):
        self.l.append(v)
        self.length += 1
        is_even = self.length % 2 == 0

        if self.median == None:
            self.median = v
            self.before.heappush(v)
        elif is_even:
            if v >= self.median:
                self.after.heappush(v)
                self.median = (self.before[0] + self.after[0]) / 2.0
            else:
                self.after.heappush(self.before.heappop())
                self.before.heappush(v)
                self.median = (self.before[0] + self.after[0]) / 2.0
        else:
            if v > self.after[0]:
                self.before.heappush(self.after.heappop())
                self.after.heappush(v)
                self.median = self.before[0]
            elif v < self.before[0]:
                self.median = self.before[0]
                self.before.heappush(v)
            else:
                self.median = v
                self.before.heappush(v)

        a = 1

    def remove(self):
        if self.length == 0:
            raise Exception("Can not remove from empty list")
            
        is_even = self.length % 2 == 0
        removed = None

        if self.length == 1:
            self.median = None
            self.before.heappop()
            return

        if is_even:
            removed = self.before.heappop()
            self.median = self.after.heappop()
            self.before.heappush(self.median)
        else:
            removed = self.before.heappop()
            self.median = (self.before[0] + self.after[0]) / 2.0

        self.length -= 1
        self.l.remove(removed)
        


r = rand(10, 100, 19)

print(r)

r = [17, 87, 46, 40, 26, 78, 66, 62, 82, 53, 59, 11, 88, 96, 42, 84, 83, 61, 26]

l = ListWithMedian()

for x in r:
    l.insert(x)
    print(l.median-median(l.l))
    
for x in range(len(r)-1):
    l.remove()
    print(l.median - median(l.l))



