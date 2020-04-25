from collections import defaultdict, deque


def cal_cost(child, f, g, cu, pu, u, flag):

    g_sum = sum([g[v] for v in child])
    fg_child = [f[v] - g[v] for v in child]
    fg_child.sort()
    f_sum = sum(fg_child[:cu])
    #print child, flag, g_sum, fg_child, cu, f_sum, pu
    if flag == 'f':
        f[u] = min(pu, f_sum) + g_sum
    else:
        g[u] = min(pu, f_sum) + g_sum


def tree_traversal(graph, P, C, root):
    '''tree traversal using post order traversal iteratively'''
    q = deque([root])
    f = [0] * (n + 1)
    g = [0] * (n + 1)
    # three levels in visit 0 - not visited, 1 - visited to add child to queue need to solve, 2 - solved
    vi = [0] * (n + 1)
    while len(q) > 0:
        u = q[-1]
        if vi[u] == 0:
            for v in graph[u]:
                if vi[v] == 0:
                    q.append(v)
            vi[u] = 1
        elif vi[u] == 1:
            q.pop()
            child = []
            for v in graph[u]:
                if vi[v] == 2:
                    child.append(v)

            if len(child) == 0:
                # boundary case for leaf
                f[u] = P[u]
                g[u] = 0
            elif u == root:
                # for root since no parent we cant select parent so only f[u] needs to calculated
                cal_cost(child, f, g, C[u], P[u], u, 'f')
            else:
                # for tree node calculating both f[u] and g[u]
                cal_cost(child, f, g, C[u], P[u], u, 'f')
                cal_cost(child, f, g, C[u] - 1, P[u], u, 'g')
            vi[u] = 2

    #print f, g
    return f[root]


t = input()
for a0 in xrange(t):
    n = input()
    graph = defaultdict(set)
    root = 1
    for a1 in xrange(n - 1):
        u, v = map(int, raw_input().split())
        graph[u].add(v)
        graph[v].add(u)
    P = [0] + map(int, raw_input().split())
    C = [0] + map(int, raw_input().split())
    print tree_traversal(graph, P, C, root)