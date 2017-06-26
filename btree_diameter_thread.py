class Node():
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

#insertion in a bst

# recursively
def insert_recur(root,value):
    if value>root.val:
        if root.right==None:
            root.right=Node(value)
        else:
            insert_recur(root.right,value)
    else:
        if root.left==None:
            root.left=Node(value)
        else:
            insert_recur(root.left,value)

# iteratively
def insert_iter(root,value):
    while 1:
        if value>root.val:
            if root.right==None:
                root.right=Node(value)
                break
            else:
                root=root.right
        else:
            if root.left==None:
                root.left=Node(value)
                break
            else:
                root=root.left

# inorder traversal in bst

# recursively - treating both leaves and internal nodes as internal nodes
def inorder_recur(root):
    if root==None:
        return
    inorder_recur(root.left)
    print root.val,
    inorder_recur(root.right)

# iteratively
def inorder_iter(root):
    stack=[root]
    vi={}
    while(stack!=[]):
        node=stack.pop()
        if node in vi:
            print node.val,
        else:
            if node.right!=None:
                stack.append(node.right)
            stack.append(node)
            if node.left!=None:
                stack.append(node.left)
            vi[node]=1

#height

# recursively
def height_recur(root):
    if root==None:
        return 0
    return 1+max(height_recur(root.left),height_recur(root.right))

# iteratively
def height_iter(root):
    stack=[(root,1)]
    maxi=1
    while(stack!=[]):
        node,depth=stack.pop()
        maxi=max(depth,maxi)
        if node.right!=None:
            stack.append((node.right,depth+1))
        if node.left!=None:
            stack.append((node.left,depth+1))
    return maxi

#diameter
def diameter(root):
    if root==None:
        return 0,0
    lheight,ldiameter=diameter(root.left)
    rheight,rdiameter=diameter(root.right)
    d = max(ldiameter,rdiameter,lheight+rheight+1)
    h = 1+max(lheight,rheight)
    return h,d

# inorder successor
# consider two cases
# 1. if right child is None, in this you have to look for successor in its ancestors where when traversing down the tree the closer ancestor where we take left from the
#ancestor to get to this node
#2. if right child is not None then the successor is min node in the right child tree, go as left as possible in the right child tree
def inorder_successor(root,node):
    succ=[None]
    if node.right==None:
        right_ancestor(root,node,succ)
    else:
        succ[0] = find_min(node.right)
    return succ[0]

def right_ancestor(root,node,succ):
    if root.val==node.val:
        return
    if node.val>root.val:
        right_ancestor(root.right,node,succ)
    else:
        succ[0]=root
        right_ancestor(root.left, node, succ)

# used to find min in the whole tree or any sub tree
def find_min(root):
    if root.left==None:
        return root
    return find_min(root.left)

# delete a element in a bst








#no of nodes as input
n=input()

values = map(int,raw_input().split())

# first value as root node
root=Node(values[0])

for a0 in values:
    if a0==root.val:
        continue
    insert_recur(root,a0)



# testing
inorder_iter(root)
print
#print height_recur(root)
print height_iter(root)
print diameter(root)
node=root.right.right
print inorder_successor(root,node).val
#diameter(root)

