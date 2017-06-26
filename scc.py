from collections import defaultdict,deque

def reverse(graph):
    r_graph=defaultdict(list)
    for u in graph.keys():
        for v in graph[u]:
            r_graph[v].append(u)
    return r_graph

def DFS(graph,vi,u,stack):
    vi[u]=1
    for v in graph[u]:
        if vi[v]==0:
            DFS(graph,vi,v,stack)
    stack.append(u)

def DFS_out(graph,vi,u):
    vi[u]=1
    print u,
    for v in graph[u]:
        if vi[v]==0:
            DFS_out(graph,vi,v)

n,m=map(int,raw_input().split())
graph = defaultdict(list)
while(m>0):
    u,v = map(int,raw_input().split())
    graph[u].append(v)
    m-=1
vi = defaultdict(int)
stack = deque()
#print graph
#DFS through all nodes and arranging the blocks of scc's in topological order in stack
for u in graph.keys():
    for v in graph[u]:
        if vi[v]==0:
            DFS(graph,vi,v,stack)
# reversing the directed graph that is u->v changes to v->u this changes a source to sink and vice versa
r_graph = reverse(graph)

# print each sink and marking it
vi.clear()
print vi
print stack
while(len(stack)>0):
    source = stack.pop()
    if vi[source]==0:
        DFS_out(r_graph,vi,source)
        print ""