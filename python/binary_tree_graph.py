from collections import defaultdict

def inorder(root,tree,colors,anc_colors,node_colors):
    color_root=colors[node_colors[root]]
    if color_root!=0:
        prev = color_root
        anc_colors[root]=color_root
    else:
        prev=0
        anc_colors[root]=-1
    colors[node_colors[root]]=root
    for node in tree[root]:
        inorder(node,tree,colors,anc_colors,node_colors)
    colors[node_colors[root]]=prev

def f(x,y):
    return (int(x),int(y))

n,c = map(int,raw_input().split())
nodes=map(f,raw_input().split(),xrange(2,n+1))
node_colors=dict(map(f,xrange(1,n+1),raw_input().split()))
tree=defaultdict(set)
for node in nodes:
    parent,child = node
    tree[parent].add(child)
colors = defaultdict(int)
anc_colors={}
root=1
inorder(root,tree,colors,anc_colors,node_colors)
print -1,
for i in xrange(2,n+1):
    print anc_colors[i],
