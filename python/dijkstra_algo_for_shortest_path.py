from collections import defaultdict
import heapq as pq
import sys

def dijkstra(graph,root):
    heap=[]
    distances = {}
    for i in xrange(1, n + 1):
        if i==root:
            distances[i]=0
        else:
            distances[i] = sys.maxint

    pq.heappush(heap,(0,root))
    visited=set()
    while(len(heap)!=0):
        d_r,r = pq.heappop(heap)
        if r not in visited:
            visited.add(r)
            for v in graph[r]:
                d_v=d_r+graph[r][v]
                if d_v<distances[v]:
                    distances[v]=d_v
                    pq.heappush(heap,(d_v,v))

    return distances

n,m = map(int,raw_input().split())

graph = defaultdict(dict)

while(m>0):
    x,y,w=map(int,raw_input().split())
    graph[x][y]=w
    graph[y][x]=w
    m-=1

print dijkstra(graph,1)
