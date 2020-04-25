#solving using segment tree
from collections import defaultdict, deque
from random import randrange
from time import time


def bs_floor(arr, l, r, val):
    # -1 to n - 1
    while r - l > 1:
        mid = (l + r) / 2
        if arr[mid] <= val:
            l = mid
        else:
            r = mid
    return l


def euler_tour(tree, n):
    q = deque([1])
    vi = [0] * (n + 1)
    occur = [-1] * (n + 1)
    path = []
    while len(q) > 0:
        u = q[-1]
        if vi[u] == 0:
            for v in tree[u]:
                if vi[v] != 1:
                    q.extend([v, u])
            vi[u] = 1
        if vi[u] == 1:
            path.append(u)
            if occur[u] == -1: occur[u] = len(path) - 1
            q.pop()
    arr = [0] * (len(path) - 1)
    for i in xrange(len(path) -1):
        arr[i] = tree[path[i]][path[i + 1]]
    return occur, arr


def f(x, y):
    #merging two array
    n, m = len(x), len(y)
    arr = [0] * (n + m)
    arr[:n] = x
    arr[n: n + m] = y
    arr.sort()
    arr1 = arr[:]
    for i in xrange(1, n + m):
        arr1[i] ^= arr1[i - 1]
    return arr, arr1


def build(seg_tree, n):
    for i in reversed(xrange(1, n)):
        seg_tree[i] = f(seg_tree[2 * i][0], seg_tree[2 * i + 1][0])


def f1(arr, arr1, k):
    n = len(arr)
    if n == 1:
        if arr[0] <= k:
            return arr[0]
        else:
            return 0
    if k < arr[0]:
        return 0
    elif k >= arr[-1]:
        return arr1[-1]
    else:
        p = bs_floor(arr, -1, n, k)
        #p = (0 + n) / 2
        return arr1[p]


def query(seg_tree, l, r, k, n):
    #l and r inclusive
    res = 0
    l, r = l + n, r + n
    while l <= r:
        if l % 2 != 0:
            res ^= f1(seg_tree[l][0], seg_tree[l][1], k)
            l += 1
        if r % 2 == 0:
            res ^= f1(seg_tree[r][0], seg_tree[r][1], k)
            r -= 1
        if l == r:
            break
        l, r = l / 2, r / 2
    return res

#t = input()
t = 5
t2, t3 = 0, 0
for a0 in xrange(1, t + 1):
    #n = input()
    #tree = defaultdict(dict)
    #for a1 in xrange(n - 1):
    #    u, v, w = map(int, raw_input().split())
    #    tree[u][v] = w
    #    tree[v][u] = w
    #occur, arr = euler_tour(tree, n)
    #n = len(arr)
    n = 2 * 10 ** 5
    arr = [randrange(10 ** 0, 10 ** 9) for i in xrange(n)]
    t1 = time()
    seg_tree = [0] * (2 * n)
    for i in xrange(n):
        seg_tree[n + i] = [[arr[i]], [arr[i]]]
    build(seg_tree, n)
    t2 += time() - t1
    #print arr
    #print seg_tree

    #m = input()
    t1 = time()
    m = 10 ** 5
    for a1 in xrange(1, m + 1):
        #u, v, k = map(int, raw_input().split())
        #i1, i2 = occur[u], occur[v]
        i1 = randrange(0, n)
        i2 = randrange(i1, n)
        k = randrange(10 ** 0, 10 ** 9)
        if i1 > i2: i1, i2 = i2, i1
        query(seg_tree, i1, i2 - 1, k, n)
    t3 += time() - t1
print t2, t3, t2 + t3