#steps
#1. create graph
#2. find degree of all nodes
#3. find all pair shortest paths
#4. check condition for all non - adjacent pairs
from collections import defaultdict, deque


def bfs(x, graph, distances):
    '''for finding all pair shortest paths'''
    q = deque([x])
    distances[(x, x)] = 0
    vi = defaultdict(int)
    while len(q) > 0:
        u = q.pop()
        for v in graph[u]:
            if vi[v] == 0:
                distances[(x, v)] = distances[(x, u)] + 1
                q.appendleft(v)
                vi[v] = 1
    return vi


def check_hamilton(graph, degree, distances, n):
    '''using Rahman-Kaykobad'''
    for u in graph:
        for v in graph:
            if u != v and v not in graph[u]:
                if degree[u] + degree[v] + distances[(u, v)] < n + 1:
                    print distances[(u, v)]
                    print u, v
                    return 'no'
    return 'yes'


t = input()
edges0 = [(1, 0), (0, 1), (0, -1)]
edges1 = [(0, 1), (-1, 0), (0, -1)]
for a0 in xrange(t):
    n = input()
    rows = [raw_input() for i in xrange(2)]
    graph = defaultdict(set)
    degree = defaultdict(int)
    # creating graph and counting degree
    edges = edges0
    n1 = 0
    for i in xrange(2):
        if i == 1:
            edges = edges1
        for j in xrange(n):
            if rows[i][j] == '#':
                n1 += 1
                for (di, dj) in edges:
                    ni = i + di
                    nj = j + dj
                    if (ni == 0 or ni == 1) and (0 <= nj < n) and rows[ni][nj] == '#':
                        graph[(i, j)].add((ni, nj))
                        degree[(i, j)] += 1
    #print graph
    #print degree
    n = n1
    print n
    distances = defaultdict(int)
    # finding all pair shortest paths and connectivity of graph
    check = 0
    for node in graph:
        if check == 0:
            vi = bfs(node, graph, distances)
            #print vi
            if len(vi) < n:
                print 'yo'
                break
            check = 1
        else:
            bfs(node, graph, distances)
    # checking hamilton path in graph
    print degree
    if check == 1:
        print check_hamilton(graph, degree, distances, n)





