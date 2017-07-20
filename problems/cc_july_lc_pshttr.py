#solving using segment tree range update point query
from collections import defaultdict, deque
from random import randrange
from time import time
from operator import itemgetter as it


def bs_floor(arr, l, r, val):
    # -1 to n - 1
    while r - l > 1:
        mid = (l + r) / 2
        if arr[mid][1] <= val:
            l = mid
        else:
            r = mid
    return l


def euler_tour(tree, edges, n):
    q = deque([1])
    vi = [0] * (n + 1)
    occur = [[-1, -1] for i in xrange(n + 1)]
    path = []
    while len(q) > 0:
        u = q[-1]
        if vi[u] == 0:
            for v in tree[u]:
                if vi[v] != 1:
                    q.extend([v, u])
                    edges.append((v, tree[v][u]))
            vi[u] = 1
        if vi[u] == 1:
            path.append(u)
            if occur[u][0] == -1: occur[u][0] = len(path) - 1
            occur[u][1] = len(path) - 1
            q.pop()

    return occur


def update(seg_tree, l, r, w, n):
    #l and r inclusive
    l, r = l + n, r + n
    while l <= r:
        if l % 2 != 0:
            seg_tree[l] ^= w
            l += 1
        if r % 2 == 0:
            seg_tree[r] ^= w
            r -= 1
        if l == r:
            break
        l, r = l / 2, r / 2


def query(seg_tree, p, n):
    p += n
    res = 0
    while p > 0:
        res ^= seg_tree[p]
        p /= 2
    return res


t = input()
for a0 in xrange(1, t + 1):
    #initialization
    n = input()
    old_n = n
    tree = defaultdict(dict)
    edges = []
    for a1 in xrange(n - 1):
        u, v, w = map(int, raw_input().split())
        tree[u][v] = w
        tree[v][u] = w
    #preprocessing
    occur = euler_tour(tree, edges, n)
    edges.sort(key=it(1))
    n = 2 * (n - 1)
    seg_tree = [0] * (2 * n)

    m = input()
    queries = []
    for a1 in xrange(1, m + 1):
        u, v, k = map(int, raw_input().split())
        queries.append((u, v, k, a1))
    queries.sort(key=it(2))
    #offline query answering
    answers = [0] * (m + 1)
    prev_p = -1
    for q in queries:
        u, v, k, a1 = q
        p = bs_floor(edges, -1, len(edges), k)
        if p != -1:
            for i in xrange(prev_p + 1, p + 1):
                node = edges[i][0]
                update(seg_tree, occur[node][0], occur[node][1], edges[i][1], n)
            ans = query(seg_tree, occur[u][0], n) ^ query(seg_tree, occur[v][0], n)
            prev_p = p
        answers[a1] = ans

    for i in xrange(1, m + 1):
        print answers[i]