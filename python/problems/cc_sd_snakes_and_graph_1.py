from collections import defaultdict
from operator import itemgetter as it


def find_parent(parent, u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u


def union(parent, rank, u, v):
    pu = find_parent(parent, u)
    pv = find_parent(parent, v)
    if pu == pv:
        return 0
    if rank[pu] < rank[pv]:
        pu, pv = pv, pu

    parent[pv] = pu
    rank[pu] += rank[pv]
    rank[pv] = 0
    return 1


t = int(raw_input().strip())
for a0 in xrange(t):
    n, m = map(int, raw_input().strip().split())

    graph = defaultdict(set)
    edges = []
    for a1 in xrange(m):
        u, v = map(int, raw_input().split())
        edges.append((u, v))
        graph[u].add(v)
        graph[v].add(u)
    degree = [0] * (n + 1)
    # calculating degree
    for i in xrange(1, n + 1):
        degree[i] = len(graph[i])
    #print degree
    e_degree = [0] * m
    ec_degree = [0] * n

    for i in xrange(m):
        e_degree[i] = edges[i], min(degree[edges[i][0]], degree[edges[i][1]])
    e_degree.sort(key=it(1), reverse=True)
    #print e_degree
    parent = [i for i in xrange(n + 1)]
    rank = [1 for i in xrange(n + 1)]

    for edge in e_degree:
        if union(parent, rank, *edge[0]):
            ec_degree[edge[1]] += 1

    for i in xrange(1, n + 1):
        if rank[i] != 0:
            ec_degree[0] += 1

    ec_degree[0] -= 1
    #print ec_degree
    prefix_ec_degree = [0] * n
    prefix_ec_degree[0] = ec_degree[0]

    print prefix_ec_degree[0],
    for i in xrange(1, n):
        prefix_ec_degree[i] = prefix_ec_degree[i - 1] + ec_degree[i]
        print prefix_ec_degree[i],
    print