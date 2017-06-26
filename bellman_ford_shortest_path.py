import sys
n,e = map(int,raw_input().split())
j=e
edges=[]
while(j>0):
    edges.append(map(int,raw_input().split()))
    j-=1

root=1
distances={}
for i in xrange(1, n + 1):
    if i == root:
        distances[i] = 0
    else:
        distances[i] = sys.maxint

i = n-1
while(i>0):
    for edge in edges:
        if distances[edge[1]]>distances[edge[0]]+edge[2]:
            distances[edge[1]]=distances[edge[0]]+edge[2]
    i-=1

for edge in edges:
    if distances[edge[1]]>distances[edge[0]]+edge[2]:
        print "beware negative cycle: "+str(edge[1])
print distances