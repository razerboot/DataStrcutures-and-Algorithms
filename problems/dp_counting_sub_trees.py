#subtree is tree rooted at u including all nodes, where as sub tree is rooted at u not all nodes are included
#counting all sub trees
#two types of sub trees rooted at a node, not rooted at node but formed by the children of node
from collections import defaultdict, deque


def count_sub_trees(tree, root, n):
    q = deque([root])
    vi = [0] * (n + 1)
    # sub trees rooted at node
    f = [0] * (n + 1)
    # sub trees not rooted of node
    g = [0] * (n + 1)
    while len(q) > 0:
        u = q[-1]
        if vi[u] == 0:
            q.extend([v for v in tree[u] if vi[v] == 0])
            vi[u] = 1
        elif vi[u] == 1:
            q.pop()
            f[u] = 1
            for v in tree[u]:
                if vi[v] == 2:
                    f[u] *= (1 + f[v])
                    g[u] += f[v] + g[v]
            vi[u] = 2
    return f[root] + g[root]

n = input()
tree = defaultdict(set)
for a0 in xrange(n - 1):
    u, v = map(int, raw_input().split())
    tree[u].add(v)
    tree[v].add(u)
print count_sub_trees(tree, 1, n)