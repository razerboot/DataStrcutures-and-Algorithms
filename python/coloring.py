from collections import defaultdict

def check(i,u,graph,vi):
    for v in graph[u]:
        if i==vi[v]:
            return False
    return True

def next_node(u,graph,vi):
    for v in graph[u]:
        if vi[v]==0:
            return v

def coloring(graph,u,n,vi,k):
    if n==0:
        return True
    for i in xrange(1,k+1):
        if check(i,u,graph,vi) and vi[u]==0:
            vi[u]=i
            v=next_node(u,graph,vi)
            if coloring(graph,v,n-1,vi,k):
                return True
            vi[u]=0
    return False
n,m,k=map(int,raw_input().split())
graph=defaultdict(set)
vi=defaultdict(int)
while(m>0):
    u,v=map(int,raw_input().split())
    graph[u].add(v)
    graph[v].add(u)
    m-=1


print coloring(graph,0,n,vi,k)
print vi



