# undirected graphs
# bfs, dfs - good
# checking loop exists - good



#connectivity
#connected components - good
# articulation points - avg
# bridges - avg
#biconnected components - avg

#directed
#strongly connected graph,components - kosaraju algo - bad


# topological sort - bad
# graph with weights 0 or 1 - shortest path - bad
#

#weighted graphs
# shortest path algos dikshtra - good, bellman ford - bad
# minimum spamming tree - avg


# bellman ford algorithm
def bellman(edges,vertex,n):
    import sys
    distances=[sys.maxint]*(n+1)
    distances[vertex]=0
    for a0 in xrange(1,n-1):
        for edge in edges:
            u,v,w=edge
            if distances[v]>distances[u]+w:
                distances[v]=distances[u]+w
    return distances[1:]

#input
n,m=map(int,raw_input().split())
edges=[]
while 1:
    edge=map(int,raw_input().split())
    if edge==None:
        break
    edges.append(edge)

print ' '.join(map(str,bellman(edges,1,n)))