from operator import itemgetter as it


def root(p, v):
    while v != p[v]:
        p[v] = p[p[v]]
        v = p[v]
    return v


def union(p, rank, x, y, w):
    root_x = root(p, x)
    root_y = root(p, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            p[root_y] = root_x
            rank[root_x] += rank[root_y]
        else:
            p[root_x] = root_y
            rank[root_y] += rank[root_x]
        return 1
    return 0


n, m = map(int, raw_input().split())

p = [i for i in xrange(n + 1)]
rank =[1 for i in xrange(n + 1)]
edges = []
for a0 in xrange(m):
    x, y, w = map(int, raw_input().split())
    edges.append((x, y, w))


edges.sort(key=it(2))
w = 0
for edge in edges:
    w += union(p, rank, *edge) * edge[2]

print w


