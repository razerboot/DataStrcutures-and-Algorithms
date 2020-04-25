#import heapq as pq
from collections import defaultdict,deque,Counter

def bfs(co_d,graph,u):
    c=Counter()
    vi=defaultdict(int)
    c[u]=0
    q=deque([u])
    while(len(q)>0):
        x=q.pop()
        if vi[x]==0:
            vi[x]=1
            for v in graph[x]:
                if vi[v]==0:
                    c[v]=c[x]+1
                    q.appendleft(v)
    co_d[u]=c
    return c
graph = defaultdict(set)
v,q=map(int,raw_input().split())
co_d={}
n=v-1
while(n>0):
	x,y = map(int,raw_input().split())
	graph[x].add(y)
	graph[y].add(x)
	n-=1

while(q>0):
    kv=map(int,raw_input().split())
    k=kv[0]
    c=Counter()
    while(k>0):
        if kv[k] in co_d:
            if c==Counter():
                c=co_d[kv[k]]
            else:
                c&=co_d[kv[k]]
        else:
            if c==Counter():
                c = bfs(co_d, graph, kv[k])
            else:
                c&=bfs(co_d,graph,kv[k])
        k-=1
    print c.most_common(1)[0][1]
    q-=1
