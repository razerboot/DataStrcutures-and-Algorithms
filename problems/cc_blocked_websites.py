
class Node():
    def __init__(self):
        self.is_leaf = 0
        # c is children
        self.c = [0]*26


def insert(root, s):
    p = 0
    n = len(s)
    while(p < n):
        key  = ord(s[p]) - 97
        if root.c[key] == 0:
            root.c[key] = Node()
        root = root.c[key]
        p += 1
    root.is_leaf = 1


def search(root1, root2, arr, prefix_arr, char_arr):
    if root1.is_leaf == 1:
        return -1
    for i in xrange(26):
        if root1.c[i] != 0 and root2.c[i] == 0:
            prefix_arr.append(char_arr[i])
            arr.append(''.join(prefix_arr))
            prefix_arr.pop()
        elif root1.c[i] != 0 and root2.c[i] != 0:
            prefix_arr.append(char_arr[i])
            if search(root1.c[i], root2.c[i], arr, prefix_arr, char_arr) == -1:
                return -1
            prefix_arr.pop()
    return 0
temp = 'abcdefghijklmnopqrstuvwxyz'
char_arr = list(temp)
q = input()
unblocked = []
blocked = []
for a0 in xrange(q):
    type, string = raw_input().strip().split()
    if type == '-':
        blocked.append(string)
    else:
        unblocked.append(string)

root1 = Node()
root2 = Node()
for ele in unblocked:
    insert(root2, ele)
for ele in blocked:
    insert(root1, ele)

#print root1.c
#print root2.c

arr =[]
prefix_arr = []
if search(root1, root2, arr, prefix_arr, char_arr) == -1:
    print -1
else:
    print len(arr)
    for ele in arr:
        print ele
