from collections import deque
from collections import defaultdict
#no of vertices
n=input()

graph=defaultdict(set)


#bfs in graph from any node
def BFS(x,graph):
    c = {}
    get=c.get
    q=deque([x])
    c[x]=0
    while(len(q)>0):
        i = q.pop()
        print i,
        for v in graph[i]:
            if get(v,-1)==-1:
                q.appendleft(v)
                c[v]=c[i]+1
    print c
    print ""
def DFS(x,graph):
    c=defaultdict(int)
    q=deque([x])
    c[x]=1
    while(len(q)>0):
        i=q.pop()
        print i,
        for v in graph[i]:
            if c[v]==0:
                q.append(v)
                c[v]=c[i]+1
    print c
#assuming 0 based numbering for vertices
# no of edges
e = input()
i=e
while(i>0):
    v_i,v_j=map(int,raw_input().split())
    graph[v_i].add(v_j)
    graph[v_j].add(v_i)
    i-=1

BFS(0,graph)
DFS(0,graph)


w = {}
w.va