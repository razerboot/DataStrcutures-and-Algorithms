# not correct for printing left-view and right-view
#do bfs and print first and last node at each level

def traverse(n, node, tree, nodes, direc):
    child = node * 2, node * 2 + 1
    if tree[node] not in nodes:
        nodes.append(tree[node])
    #print child
    if (child[0] > n and child[1] > n) or (tree[child[0]] == 0 and tree[child[1]] == 0):
        return
    if tree[child[direc]] != 0:
        traverse(n,child[direc], tree, nodes, direc)
    else:
        traverse(n,child[1 - direc], tree, nodes, direc)


# direc 0 - left
# direc 1 - right
t = input()
for a0 in xrange(t):
    n = input()
    tree = [0] + list(map(int, raw_input().split()))
    nodes = []
    traverse(n, 1, tree, nodes, 1)
    traverse(n, 1, tree, nodes, 0)
    for ele in nodes:
        print ele
    print