from collections import defaultdict, deque
from time import time
from random import randrange


def dfs(graph, parents, vi):
    q = deque([1])
    while len(q) > 0:
        u = q.pop()
        if vi[u] == 0:
            vi[u] = 1
            for v in graph[u]:
                if vi[v] == 0:
                    q.append(v)
                    parents[v] = parents[u].copy()
                    parents[v].add(u)


graph1 = defaultdict(set)
graph2 = defaultdict(set)
parents1 = defaultdict(set)
parents2 = defaultdict(set)
t = input()
for a0 in xrange(t):
    n = input()
    graph1.clear()
    graph2.clear()
    parents1.clear()
    parents2.clear()
    for i in xrange(n - 1):
        u, v = map(int, raw_input().split())
        graph1[u].add(v)
        graph1[v].add(u)

    for i in xrange(n - 1):
        u, v = map(int, raw_input().split())
        graph2[u].add(v)
        graph2[v].add(u)
    vi = [0] * (n + 1)
    dfs(graph1, parents1, vi)
    vi = [0] * (n + 1)
    dfs(graph2, parents2, vi)
    #print parents1
    #print parents2
    for i in xrange(1, n + 1):
        print len(parents1[i] & parents2[i]),
    print

