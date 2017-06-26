import heapq as pq
from collections import defaultdict, deque
import sys


def dijk(graph, r, distances):
    parent=[]
    heap = []
    heap.append((0, r))
    vi = set()
    while len(heap) > 0:
        d_r, r = pq.heappop(heap)
        if r not in vi:
            vi.add(r)
            for k in graph[r]:
                d_v = d_r + graph[r][k]
                if d_v < distances[k]:
                    pq.heappush(heap, (d_v, k))
                    distances[k] = d_v


graph = defaultdict(dict)
n, m = map(int, raw_input().split())
v = n * m
e = (v * (v - 1)) / 2
i = n
arr = []
distances = {}
distances[0] = 0
while (i > 0):
    arr.append(map(int, raw_input().split()))
    i -= 1
moves = [(0, 1), (1, 0), (1, 1)]
for i in xrange(n):
    for j in xrange(m):
        p = (m * i) + j
        for ele in moves:
            new_i = i + ele[0]
            new_j = j + ele[1]
            if 0 <= new_i < n and 0 <= new_j < m:
                r = m * (new_i) + new_j
                l = m * (i) + j
                k = abs(arr[i][j] - arr[new_i][new_j])
                graph[r][l] = k
                graph[l][r] = k

for i in xrange(1, v):
    distances[i] = sys.maxint
dijk(graph, 0, distances)
print distances
