#!/bin/python
from collections import defaultdict, Counter
from fractions import Fraction as fc
import sys

def traverse(u, v, graph, t, vi):
    vi[u] = 1
    t.add(u)
    for child in graph[u]:
        if vi[child] == 0 and child != v:
            traverse(child, v, graph, t, vi)

def add_to_counter(cnt, set1, w):
    for ele in set1:
        cnt[ele] += w

def dfs(parent, child, cnt, graph, graph_count, nodes):
    t = {}
    t = set()
    vi = defaultdict(int)
    if graph_count[parent] > graph_count[child]:
        # traverse child other than parent
        traverse(child, parent, graph, t, vi)
        add_to_counter(cnt, nodes.difference(t), 1)
    else:
        # traverse parent other than child
        traverse(parent, child, graph, t, vi)
        add_to_counter(cnt, t, 1)
        # print t
        # print cnt


def find(k, cnt):
    c = 0
    for key in cnt:
        if cnt[key] >= k:
            c += 1
    return c

q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    nodes = {}
    nodes = set()
    for i in xrange(1, n + 1):
        nodes.add(i)
    graph = defaultdict(set)
    graph_count = defaultdict(int)
    for a1 in xrange(n - 1):
        u, v = map(int, raw_input().strip().split(' '))
        graph[u].add(v)
        graph_count[u] += 1
        graph[v].add(u)
        graph_count[v] += 1
    g, k = map(int, raw_input().strip().split(' '))
    cnt = Counter()
    digraph = set()
    complete = 0
    for a1 in xrange(g):
        parent, child = map(int, raw_input().strip().split(' '))
        if (child,parent) in digraph:
            complete += 1
            digraph.remove((child, parent))
        else:
            digraph.add((parent,child))
    add_to_counter(cnt, nodes, complete)
    if complete == k:
        print "1/1"
        continue
    for key in digraph:
        parent = key[0]
        child = key[1]
        if child in graph[parent]:
            dfs(parent, child, cnt, graph, graph_count, nodes)
    c = find(k, cnt)
    if c == 0:
        print "0/1"
    elif c == n:
        print "1/1"
    else:
        print fc(c, n)