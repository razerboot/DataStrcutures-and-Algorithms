#tarzan's algorithm
from collections import defaultdict

class time():
    def __init__(self,key):
        self.t=key

def find_ap(graph,dist,low,vi,p,ap,u,c,stack):
    child=0
    dist[u]=c.t
    c.t += 1
    low[u]=dist[u]
    vi[u]=1
    for v in graph[u]:
        if vi[v]==0:
            child+=1
            p[v]=u
            stack.append((u, v))
            find_ap(graph,dist,low,vi,p,ap,v,c,stack)
            low[u]=min(low[u],low[v])
            if p[u]!=-1 and low[v]>=dist[u] or p[u]==-1 and child>1:
                ap[u]=1
                while (stack[-1][0]!=u):
                    print stack.pop(),
                print stack.pop(),
                print ""
        elif vi[v]==1 and p[u]!=v:
            stack.append((u, v))
            low[u]=min(low[u],dist[v])
    vi[u]=2
# vi 0 white yet to visit vi 1 grey in function stack vi 2 visiting complete not in function stack
n,e = map(int,raw_input().split())
graph = defaultdict(set)
dist = {}
low = {}
stack=[]
vi = defaultdict(int)
p = {}
p[0]=-1
ap=defaultdict(int)
while(e>0):
    u,v= map(int,raw_input().split())
    graph[u].add(v)
    graph[v].add(u)
    e-=1
#if graph has single connected component
find_ap(graph,dist,low,vi,p,ap,0,time(0),stack)
if stack!=[]:
    while(stack!=[]):
        temp=stack.pop()
        print temp,
    print ""
#else loop through all vertices to traverse all connected components
print ap
print dist

#input

'''10 13
0 1
0 6
1 2
1 3
1 5
2 3
2 4
3 4
5 6
5 7
5 8
7 8
8 9'''
#3  703 279 43 0 0 0 1 0 1 1 1 0