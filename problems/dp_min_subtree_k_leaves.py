from collections import defaultdict, deque


def min_sub_tree(tree, C, root, n, K):
    q = deque([root])
    vi = [0] * (n + 1)
    f = [None for i in xrange(n + 1)]
    while len(q) > 0:
        u = q[-1]
        if vi[u] == 0:
            q.extend([v for v in tree[u] if vi[v] == 0])
            vi[u] = 1
        elif vi[u] == 1:
            q.pop()
            dp, dp1 = [-1] * (K + 1), [-1] * (K + 1)
            # maintaing 0 leaves when no children is costing 0, initial value of dp
            dp[0] = 0
            for v in tree[u]:
                if vi[v] != 2: continue
                for j in xrange(0, K + 1):
                    for k in xrange(0, j + 1):
                        if f[v][k] >= 0 and (dp1[j] == -1 or dp1[j] > dp[j - k] + f[v][k]):
                            dp1[j] = dp[j - k] + f[v][k]
                dp, dp1 = dp1, [-1] * (K + 1)
            if len(tree[u]) == 1:
                # leaf, maintaing 1 leaf is costing 0 since it is a leaf
                dp[1] = 0
            #adding C[u] because maintaining 0 leafs in each of children gives rise to 1 leaf because of current node
            #we need to remove that too for f[0]
            dp[0] += C[u]
            f[u] = dp
            vi[u] = 2

    return f[root][K]


n, K = map(int, raw_input().split())
C = [0] + map(int, raw_input().split())
tree = defaultdict(set)
for a0 in xrange(n - 1):
    u, v = map(int, raw_input().split())
    tree[u].add(v)
    tree[v].add(u)
print min_sub_tree(tree, C, 1, n, K)