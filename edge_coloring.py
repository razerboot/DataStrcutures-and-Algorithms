from collections import defaultdict
from fractions import gcd


def check(e, i, graph, vi, e_map, v_map):
    u, v = e_map[e]
    for node in graph[u]:
        e1 = v_map[str(u) + "#" + str(node)]
        if vi[e1] != 0 and gcd(vi[e1], i) != 1:
            return False
    for node in graph[v]:
        e1 = v_map[str(v) + "#" + str(node)]
        if vi[e1] != 0 and gcd(vi[e1], i) != 1:
            return False
    return True


def next_edge(graph, e, vi, e_map, v_map):
    u, v = e_map[e]
    for node in graph[u]:
        e1 = v_map[str(u) + "#" + str(node)]
        if vi[e1] == 0:
            return e1
    for node in graph[v]:
        e1 = v_map[str(v) + "#" + str(node)]
        if vi[e1] == 0:
            return e1


def coloring(graph, e, m, vi, e_map, v_map, num):
    if m == 0:
        return True
    for i in num:
        if check(e, i, graph, vi, e_map, v_map) and vi[e] == 0:
            vi[e] = i
            v = next_edge(graph, e, vi, e_map, v_map)
            num.remove(i)
            if coloring(graph, v, m - 1, vi, e_map, v_map, num):
                return True
            vi[e] = 0
            num.add(i)
    return False


graph = defaultdict(set)
e_map = defaultdict(tuple)
v_map = defaultdict(int)
num = set()
vi = defaultdict(int)
n, m = map(int, raw_input().split())
k = m
i = m
while (i > 0):
    x, y = map(int, raw_input().split())
    num.add(i)
    graph[x].add(y)
    graph[y].add(x)
    e_map[m - i + 1] = (x, y)
    v_map[str(x) + "#" + str(y)] = m - i + 1
    v_map[str(y) + "#" + str(x)] = m - i + 1
    i -= 1

while not coloring(graph, 1, m, vi, e_map, v_map, num):
    #print vi
    k += 1
    num.add(k)
#print vi
print k
#for i in xrange(1, m + 1):
#    print vi[i]
