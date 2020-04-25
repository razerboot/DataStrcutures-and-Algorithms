#tarzan's algorithm
from collections import defaultdict

class time():
    def __init__(self,key):
        self.t=key

def find_ap(graph,dist,low,vi,p,ap,u,c):
    dist[u]=c.t
    low[u]=dist[u]
    vi[u]=1
    for v in graph[u]:
        if vi[v]==0:
            p[v]=u
            c.t += 1
            find_ap(graph,dist,low,vi,p,ap,v,c)
            low[u]=min(low[u],low[v])
            if low[v]>dist[u]:
                ap.add(u,v)
        elif p[u]!=v:
            low[u]=min(low[u],dist[v])

n,e = map(int,raw_input().split())
graph = defaultdict(set)
dist = {}
low = {}
vi = defaultdict(int)
p = {}
p[0]=-1
ap=set
while(e>0):
    u,v= map(int,raw_input().split())
    graph[u].add(v)
    graph[v].add(u)
    e-=1
#if graph has single connected component
find_ap(graph,dist,low,vi,p,ap,0,time(0))
#else loop through all vertices to traverse all connected components
print ap
print dist
