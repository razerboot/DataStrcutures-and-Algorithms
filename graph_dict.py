import heapq as pq
from collections import defaultdict, deque

graph = defaultdict(set)


def DFS(head, graph, c):
    s = deque([head])
    while (len(s) > 0):
        i = s.pop()
        for j in graph[i]:
            if c[j] == 0:
                c[j] = 1
                s.append(j)


n, m = map(int, raw_input().split())
while (m > 0):
    x, y = map(int, raw_input().split())
    graph[x].add(y)
    graph[y].add(x)
    m -= 1

head = input()
count = 0
c = defaultdict(int)
DFS(head, graph,c)
for i in xrange(n):
    if c[i] == 0:
        count += 1
print count