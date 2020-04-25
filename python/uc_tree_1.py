#!/bin/python
from collections import defaultdict,Counter
from fractions import Fraction as fc
import sys
class count():
    def __init__(self,key):
        self.c=key
def dfs(graph,vi,u,stack):
    vi[u]=1
    for v in graph[u]:
        if vi[v]==0:
            dfs(graph,vi,v,stack)
    stack.append(u)
def reverse(graph):
    r_graph=defaultdict(list)
    for u in graph.keys():
        for v in graph[u]:
            r_graph[v].append(u)
    return r_graph
def dfs_rev(graph,vi,u,co):
    vi[u]=1
    co.c+=1
    for v in graph[u]:
        if vi[v]==0:
            dfs_rev(graph,vi,v,co)
def find(k,est):
    c=0
    for key in est:
        if key>=k:
            c+=est[key]
    return c
q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    nodes={}
    nodes=set()
    for i in xrange(1,n+1):
        nodes.add(i)
    graph=defaultdict(set)
    for a1 in xrange(n-1):
        u,v = map(int,raw_input().strip().split(' '))
        graph[u].add(v)
        graph[v].add(u)
    g,k = map(int,raw_input().strip().split(' '))
    digraph={}
    digraph=set()
    complete=0
    for a1 in xrange(g):
        parent,child = map(int,raw_input().strip().split(' '))
        if (child,parent) not in digraph:
            digraph.add((parent,child))
        else:
            complete+=1
            digraph.remove((child,parent))
    if complete==k:
        print "1/1"
        continue
    for ele in digraph:
        parent=ele[0]
        child=ele[1]
        if child in graph[parent]:
            graph[parent].remove(child)
    stack=[]
    vi = defaultdict(int)
    for i in xrange(1,n+1):
        if vi[i]==0:
            dfs(graph,vi,i,stack)
    r_graph = reverse(graph)
    vi.clear()
    lvl=1
    est={}
    while(stack!=[]):
        u = stack.pop()
        if vi[u]==0:
            co=count(0)
            dfs_rev(r_graph,vi,u,co)
            est[lvl]=co.c
            lvl+=1
    c = find(k-complete,est)
    if c==0:
        print "0/1"
    elif c==n:
        print "1/1"
    else:
        print fc(c,n)