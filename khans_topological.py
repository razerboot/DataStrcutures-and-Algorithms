from collections import defaultdict


# using khan's algo
def cyclecheck(graph, n):
    degree = [0] * (n + 1)

    for u in graph:
        for v in graph[u]:
            degree[v] += 1
    q = []
    for u in xrange(1, n + 1):
        if degree[u] == 0:
            q.append(u)
    count = 0
    while (q != []):
        u = q.pop()
        for v in graph[u]:
            degree[v] -= 1
            if degree[v] == 0:
                q.append(v)
        count += 1

    if count != n:
        return 1
    else:
        return 0


t = input()

for a0 in xrange(t):
    n, m = map(int, raw_input().split())
    graph = defaultdict(set)
    for a1 in xrange(m):
        u, v = map(int, raw_input().split())
        graph[u].add(v)
    print cyclecheck(graph, n)