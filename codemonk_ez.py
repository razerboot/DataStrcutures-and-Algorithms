from operator import itemgetter
import heapq as pq
from collections import defaultdict

t = input()
for x in xrange(t):
    v, e = map(int, raw_input().split())
    graph = defaultdict(dict)
    for f in xrange(e):
        x, y, w = map(int, raw_input().split())
        graph[x][y] = w
    q = []
    print graph
    for u in graph[1]:
        pq.heappush(q, ((-1*graph[1][u]), u))
    vi = [0] * (v + 1)
    cost=0
    while (len(q) > 0):
        e = pq.heappop(q)
        if vi[e[1]] == 1:
            continue
        cost += e[0]
        vi[e[1]] = 1
        for u in graph[e[1]]:
            if vi[u] == 0:
                pq.heappush(q, ((-1*graph[e[1]][u]), u))
        print q
    print cost*-1
