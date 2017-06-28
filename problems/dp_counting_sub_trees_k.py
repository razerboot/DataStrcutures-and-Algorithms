#subtree is tree rooted at u including all nodes, where as sub tree is rooted at u not all nodes are included
#counting all sub trees with size equal to k
#two types of sub trees rooted at a node, not rooted at node but formed by the children of node
from collections import defaultdict, deque


def count_sub_trees(tree, root, n, K):
    q = deque([root])
    vi = [0] * (n + 1)
    # each f[i] contains count of all sub trees from size 0 to K
    #f[0] is 1 since it is used for calculation of its parent where no selection is counted as 1
    #f[1] is 1 for leaf nodes since selecting 1 node is the only way possible
    f = [[1, 1] + [0] * (K - 1) for i in xrange(n + 1)]
    while len(q) > 0:
        u = q[-1]
        if vi[u] == 0:
            q.extend([v for v in tree[u] if vi[v] == 0])
            vi[u] = 1
        elif vi[u] == 1:
            q.pop()
            # finding all possible sub trees of size K - 1 rooted at u(since u is counted for 1 node in the sub tree),
            dp1 = [0] * K
            flag = 0
            for v in tree[u]:
                if vi[v] == 2:
                    if flag == 0:
                        dp = f[v][:-1]
                        flag = 1
                        continue
                    for j in xrange(K):
                        for k in xrange(j + 1):
                            dp1[j] += dp[j - k] * f[v][k]
                dp = dp1
            if flag == 1:
                #not leaf
                f[u][1:] = dp
            vi[u] = 2
    total_k = 0
    for i in xrange(1, n + 1):
        total_k += sum(f[i])
    return total_k - n

n, K = map(int, raw_input().split())

tree = defaultdict(set)
for a0 in xrange(n - 1):
    u, v = map(int, raw_input().split())
    tree[u].add(v)
    tree[v].add(u)
print count_sub_trees(tree, 1, n, K)