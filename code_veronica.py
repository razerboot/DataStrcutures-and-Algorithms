# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque


class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.index = None
        self.suc = None
        self.pre = None


class BST():
    def __init__(self):
        self.root = None

    def insert(self, m, node, head, arr):
        parent = None
        current = head
        succ = None
        pred = None
        while (current):
            if node.val > current.val:
                pred = current
                parent = current
                current = current.right
            else:
                succ = current
                parent = current
                current = current.left
        j = parent.index
        if parent.val > node.val:
            k = (2 * j) % m
            node.index = k
            node.suc = parent
            node.pre = pred
            parent.left = node
        else:
            k = ((2 * j) % m + 1) % m
            node.index = k
            node.suc = succ
            node.pre = parent
            parent.right = node
        arr.append(str(k))
        # return node


size = int(raw_input())
arr = raw_input().strip().split(' ')

b_tree = BST()
m = (10 ** 9) + 7
arr1 = deque()

temp = Node(int(arr[0]))
temp.index = 1
b_tree.root = temp
arr1.append("1")

i = 1
mini = b_tree.root
maxi = b_tree.root
prev = b_tree.root
while (i < size):
    key = int(arr[i])
    temp = Node(key)
    if prev.suc and prev.val < temp.val < prev.suc.val:
        # print "yo"
        j = prev.index
        succ = prev.suc
        temp.index = ((2 * j) % m + 1) % m
        temp.suc = succ
        temp.pre = prev
        prev.right = temp
        arr1.append(str(temp.index))
    elif prev.pre and prev.pre.val < temp.val < prev.val:
        # print "yo"
        j = prev.index
        pred = prev.pre
        temp.index = (2 * j) % m
        temp.pre = pred
        temp.suc = prev
        prev.left = temp
        arr1.append(str(temp.index))
    elif temp.val > maxi.val:
        # print "hmm"
        j = maxi.index
        temp.index = ((2 * j) % m + 1) % m
        temp.pre = maxi
        maxi.right = temp
        arr1.append(str(temp.index))
        maxi = temp
    elif temp.val < mini.val:
        # print "hmm"
        j = mini.index
        temp.index = (2 * j) % m
        temp.suc = mini
        mini.left = temp
        arr1.append(str(temp.index))
        mini = temp
    else:
        b_tree.insert(m, temp, b_tree.root, arr1)
    prev = temp
    i += 1
print " ".join(list(arr1))

