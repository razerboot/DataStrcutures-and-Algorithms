from collections import defaultdict

#left view
def preorder_left(tree,heights,root,maxi,lefts):
    if root==1 or maxi[0]<heights[root]:
        lefts.add(root)
        maxi[0]=heights[root]
    elif tree[root]==[]:
        return
    for child in tree[root]:
        heights[child]=heights[root]+1
        preorder_left(tree,heights,child,maxi,lefts)

#right view
def preorder_right(tree,heights,root,maxi,rights):
    if maxi[0]<heights[root]:
        rights.add(root)
        maxi[0]=heights[root]
    elif tree[root]==[]:
        return
    temp=tree[root][::-1]
    for child in temp:
        heights[child] = heights[root] + 1
        preorder_right(tree,heights,child,maxi,rights)

#traversal visit parent, visit childs from left to right, visit parent again
def traversal(tree,lefts,rights,root):
    if tree[root]==[]:
        print root,
        return
    else:
        if root in lefts:
            print root,
    for child in tree[root]:
        traversal(tree,lefts,rights,child)
    if root in rights:
        print root,


n=input()
tree=defaultdict(list)
heights=[0]*(n+1)
lefts=set()
rights=set()
for a0 in xrange(n-1):
    u,v=map(int,raw_input().split())
    tree[u].append(v)

maxi=[1]
heights[1]=1
preorder_left(tree,heights,1,maxi,lefts)
maxi=[1]
heights=[0]*(n+1)
heights[1]=1
preorder_right(tree,heights,1,maxi,rights)
traversal(tree,lefts,rights,1)



'''
15
1 2
1 13
2 3
3 4
3 14
14 5
5 6
5 7
13 8
13 12
12 15
15 9
15 10
12 11
'''

'''
8
1 2
1 3
3 8
2 4
2 5
5 6
5 7
'''

'''
6
1 2
2 3
2 6
3 4
4 5
'''

'''
6
1 2
1 3
3 4
3 5
4 6
'''

'''
9
1 2
1 3
2 4
2 5
3 6
5 7
5 8
7 9
'''