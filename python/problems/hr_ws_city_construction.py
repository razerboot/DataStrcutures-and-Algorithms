from collections import deque, defaultdict


def dfs(graph, stack, x, vi):
    '''dfs and add elements to stack in a way of topology'''
    q = deque([x])
    while len(q) > 0:
        u = q[-1]
        #print u
        if vi[u] == 0:
            for v in graph[u]:
                if vi[v] == 0:
                    q.append(v)
            vi[u] = 1
        elif vi[u] == 1:
            q.pop()
            stack.append(u)
            vi[u] = 2
        else:
            q.pop()


def r_dfs(graph, x, vi):
    '''dfs the graph for each element of stack in reverse graph and return elements of
    one strongly connected component'''
    cc = {x}
    q = deque([x])
    while len(q) > 0:
        u = q.pop()
        cc.add(u)
        vi[u] = 1
        for v in graph[u]:
            if vi[v] == 0:
                q.append(v)
    return cc


def reach_parent(x, px, graph):
    '''from any newly added node to its parent and travelling in the direction of node with index less than it self'''
    while x is not None and x != px:
        for v in graph[x]:
            if v < x:
                x = v
                break
        else:
            x = None
    if x == px:
        return 1
    return 0


def check_reachable(x, y, graph, r_graph, parent, cc_links, can_reach):
    '''checks all possible conditions in the graph
    1. out - out - different parent
    2. out - out - same parent
    3. out - in
    4. in - in'''
    px = parent[x]
    py = parent[y]
    ccx = cc_links[px]
    ccy = cc_links[py]
    if px == py:
        b = graph
        if x < y:
            b = r_graph
            x, y = y, x
        if reach_parent(x, y, b):
            return 'Yes'
        else:
            return 'No'
    if ccx not in can_reach[ccy]:
        return 'No'
    if reach_parent(x, px, graph) == 0:
        return 'No'
    if reach_parent(y, py, r_graph) == 0:
        return 'No'
    return 'Yes'


graph = defaultdict(set)
r_graph = defaultdict(set)
new_graph = defaultdict(set)
scc = [None]
stack = []

n, m = map(int, raw_input().split())
for a0 in xrange(m):
    u, v = raw_input().split()
    u, v = int(u), int(v)
    graph[u].add(v)
    r_graph[v].add(u)

'''dfs for finding top of the graph'''
vi = [0] * (n + 1)
for i in xrange(1, n + 1):
    if vi[i] == 0:
        dfs(graph, stack, i, vi)

#print stack
''' dfs to identify scc's'''
vi = [0] * (n + 1)
cc_links = [0] * (n + 1)
while len(stack) > 0:
    u = stack.pop()
    if vi[u] == 0:
        cc = r_dfs(r_graph, u, vi)
        #print cc
        scc.append(cc)
        l = len(scc) - 1
        for ele in cc:
            cc_links[ele] = l

'''creating a new graph with scc's as nodes'''
l = len(scc)
for i in xrange(1, l):
    cc = scc[i]
    for u in cc:
        for v in graph[u]:
            if v not in cc:
                new_graph[i].add(cc_links[v])


'''for each scc finding scc's from where it can be reached'''
degree = [0] * l
for i in xrange(1, l):
    for v in new_graph[i]:
        degree[v] += 1

q = deque([])
for i in xrange(1, l):
    if degree[i] == 0:
        q.append(i)

can_reach = defaultdict(set)

while len(q) > 0:
    u = q.pop()
    can_reach[u].add(u)
    for v in new_graph[u]:
        can_reach[v] |= can_reach[u]
        degree[v] -= 1
        if degree[v] == 0:
            q.append(v)

#print new_graph
#print scc
#print cc_links
#print can_reach


new_n = n
parent = [i for i in xrange(n + 1)]
q = input()
for a0 in xrange(q):
    t, x, y = raw_input().split()
    t, x, y = int(t), int(x), int(y)
    if t == 1:
        new_n += 1
        if y == 1:
            graph[new_n].add(x)
            r_graph[x].add(new_n)
        else:
            graph[x].add(new_n)
            r_graph[new_n].add(x)
        parent.append(parent[x])
    else:
        print check_reachable(x, y, graph, r_graph, parent, cc_links, can_reach)
#print parent
