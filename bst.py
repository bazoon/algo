import random
import math
import sys
import time

sys.setrecursionlimit(15000)


class TreeNode:
    def __init__(self, parent, key):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.key = key

class BSTTree:
    def __init__(self):
        self.root = None
   
    def add(self, key):

        def aux(root):
            if (root == None):
                root = TreeNode(self.root, key)
                if self.root == None:
                    self.root = root
            else:
                if (root.key <= key):
                    if root.right_child == None:
                        root.right_child = TreeNode(root, key)
                    else:
                        aux(root.right_child)
                else:
                    if root.left_child == None:
                        root.left_child = TreeNode(root, key)
                    else:
                        root.left_child = aux(root.left_child)

            return root

        aux(self.root)

    def find(self, key):
        def aux(node):
            if node is None:
                return None
            if node.key == key:
                return node

            if node.key < key:
                return aux(node.right_child)
            else:
                return aux(node.left_child)


        return aux(self.root)


    
    
def rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res


class Tree():
    def __init__(self):
        self.items = None

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self, index):
        return 2 * index + 2

    def from_array(self, arr):
        l = len(arr)
        sorted_arr = sorted(arr)
        height = math.ceil(math.log(l, 2))
        self.items = [None] * int(math.pow(2, height + 1) - 1)
        self.from_array_helper(sorted_arr, 0, l, 0)

    def from_array_helper(self, l, start, end, index):
        m = (start + end) // 2
        self.items[index] = l[m]

        left = l[start:m]
        right = l[m + 1:end + 1]
        if (len(left) > 0):
            self.from_array_helper(l, start, m - 1, self.left_child_index(index))
        if (len(right) > 0):
            self.from_array_helper(l, m + 1, end, self.right_child_index(index))

    def find(self, value):
        def aux(index):
            if index >= len(self.items) - 1:
                return None

            if self.items[index] == value:
                return index
            elif self.items[index] is None:
                return None
            elif self.items[index] < value:
                return aux(self.right_child_index(index))
            else:
                return aux(self.left_child_index(index))

        return aux(0)



# a = sorted([1,2,3,4,5,6,7,8,9,10])

b = rand(1, 100, 1000) 
b.append(19198)
a = sorted(b)

tree = Tree()
bst_tree = BSTTree()


start = time.time()
for x in a:
    bst_tree.add(x)
end = time.time()
print("Tree (node) time: " + str((end - start)))


a = sorted(rand(1, 100, 999))

tree = Tree()
bst_tree = BSTTree()

start = time.time()
tree.from_array(a)
end = time.time()
print("Tree (array) time: " + str((end - start)))


start = time.time()
for x in a:
    bst_tree.add(x)
end = time.time()
print("Tree (node) time: " + str((end - start)))










