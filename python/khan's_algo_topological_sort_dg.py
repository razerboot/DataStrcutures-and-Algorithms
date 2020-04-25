from collections import defaultdict
def topology(graph,n):
    degree=[0]*(n+1)
    for u in graph:
        for v in graph[u]:
            degree[v]+=1
    s=[]
    for i in xrange(1,n+1):
        if degree[i]==0:
            s.append(i)
    count=0
    while(s!=[]):
        u=s.pop()
        print u,
        for v in graph[u]:
            degree[v]-=1
            if degree[v]==0:
                s.append(v)
        count+=1
    return count==n



n,m=map(int,raw_input().split())
graph=defaultdict(set)
for a0 in xrange(m):
    u,v = map(int,raw_input().split())
    graph[u].add(v)
topology(graph,n)

















