#given a Ci coins for each node in the tree find a set of nodes such that no two nodes are directly connected and
#sum of coins of respective nodes is maxmimum
from collections import deque, defaultdict


def find_maximum_coin_set(C, tree, root, n):
    q = deque([root])
    vi = [0] * (n + 1)
    #root of subtree is choosen
    dp1 = [0] * (n + 1)
    #root of subtree is not choosen
    dp2 = [0] * (n + 1)
    while len(q) > 0:
        u = q[-1]
        if vi[u] == 0:
            for v in tree[u]:
                if vi[v] == 0:
                    q.append(v)
            vi[u] = 1
        elif vi[u] == 1:
            q.pop()
            dp1[u] = C[u]
            for v in tree[u]:
                if vi[v] == 2:
                    dp1[u] += dp2[v]
                    dp2[u] += max(dp1[v], dp2[v])
            vi[u] = 2
    return max(dp1[root], dp2[root])

n = input()
C = [0] + map(int, raw_input().split())
tree = defaultdict(set)
for a0 in xrange(n - 1):
    u, v = map(int, raw_input().split())
    tree[u].add(v)
    tree[v].add(u)
print find_maximum_coin_set(C, tree, 1, n)