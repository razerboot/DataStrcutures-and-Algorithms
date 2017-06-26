from collections import defaultdict,deque,Counter
import sys
def bfs(p_g,s,h,p_n):
    if s==set([1]):
        return find_max(h[1],p_n)
    maxi=-1
    vi=defaultdict(int)
    q=deque()
    dis={}
    for v in p_n:
        dis[v]=sys.maxint
    for ele in s:
        dis[ele]=0
        q.appendleft(ele)
    while(len(q)>0):
        x=q.pop()
        if vi[x]==0:
            vi[x]=1
            d = max(dis[x],dis[x]+find_max(h[x],p_n))
            if maxi<d:
                maxi=d
            for v in p_g[x]:
                if vi[v]==0 and dis[v]>dis[x]+1:
                    dis[v]=dis[x]+1
                    q.appendleft(v)
    return maxi
def find_max(h1,p_n):
    maxi=-1
    for u,d in h1.items():
        if u not in p_n and maxi<h1[u]:
            maxi=h1[u]
    return maxi
def cal_h(h,g,t_g,r,p,vi):

    maxi=0
    vi[r]=1
    for x in t_g:
        if vi[x]==0:
            p[x]=r
            h[r][x]=1+cal_h(h,g,g[x],x,p,vi)
            if maxi<h[r][x]:
                maxi=h[r][x]
    return maxi
def p_graph(p_g,s,g,h,p):
    for v in s:
        p_n.add(v)
        while(p[v]!=0):
            p_g[v].add(p[v])
            p_g[p[v]].add(v)
            p_n.add(p[v])
            v=p[v]
p_n=set()
g =defaultdict(set)
p_g=defaultdict(set)
h=defaultdict(dict)
p=defaultdict(int)
vi=defaultdict(int)
v,q=map(int,raw_input().split())
while(v>1):
    x,y = map(int,raw_input().split())
    g[x].add(y)
    g[y].add(x)
    v-=1

cal_h(h,g,g[1],1,p,vi)

while(q>0):
    kv=map(int,raw_input().split())
    k=kv[0]
    s=set(kv[1:k+1])
    p_g.clear()
    p_n.clear()
    p_graph(p_g,s,g,h,p)
    print bfs(p_g,s,h,p_n)
    q-=1
