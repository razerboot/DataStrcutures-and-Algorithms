#under construction
#post order traversal using DP for finding longest BST in a b-tree
from collections import defaultdict, deque


def post_ot(tree, values, direc, root, n):
    q = deque([root])
    vi = [0] * (n + 1)
    l = [i for i in xrange(n + 1)]
    r = [i for i in xrange(n + 1)]
    size = [1] * (n + 1)
    while len(q) > 0:
        u  = q[-1]
        if vi[u] == 0:
            for v in tree[u]:
                q.append(v)
            vi[u] = 1
        elif vi[u] == 1:
            u = q.pop()
            for v in tree[u]:
                if vi[v] == 2 and direc[v] == 'l':















n = input()
tree = defaultdict(set)
values = map(int, raw_input().split())
direc = ['n','n'] + raw_input().split()
for a0 in xrange(n - 1):
    u, v = map(int, raw_input().split())
    tree[u].add(v)
    tree[v].add(u)


