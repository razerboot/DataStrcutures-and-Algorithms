import re
from collections import deque
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

class Btree:
    def __init__(self):
        self.head = None

    def add_node(self,p_val,c_val,direction):
        node = Node(c_val)
        p_pointer=self.head
        if p_pointer==None:
            self.head = Node(p_val)
            p_pointer = self.head
        else:
            p_pointer = self.find_p(p_val,p_pointer)
        if direction == "R" and p_pointer != None:
            p_pointer.right = node
        elif p_pointer != None:
            p_pointer.left = node

    def find_p(self,value,head):
        if head==None:
            return None
        if head.val==value:
            return head
        left = self.find_p(value, head.left)
        right = self.find_p(value, head.right)
        if left!=None:
            return left
        if right!=None:
            return right
        return None

    #DFS
    def traverse_inorder(self,head,arr):
        if head==None:
            return
        self.traverse_inorder(head.left,arr)
        arr.append(head.val)
        self.traverse_inorder(head.right,arr)
        return

    #leaves using DFS
    def leaves(self,head,arr):
        if head==None:
            return
        if head.left==None and head.right==None:
            arr.append(head.val)
        self.leaves(head.left,arr)
        self.leaves(head.right,arr)

    #inorder traversal without recursion
    def inorderTraversal(self, A):
        from collections import deque
        arr = [A]
        arr1 = {}
        get = arr1.get
        order = []
        while (len(arr) != 0):
            root = arr.pop()
            s = get(root, -1)
            if s == 1:
                order.append(root.val)
            else:
                if root.right != None:
                    arr.append(root.right)
                arr.append(root)
                if root.left != None:
                    arr.append(root.left)
                arr1[root] = 1
        return order

    #using BFS for leaves and traversal
    def traverse_bfs(self):
        head = self.head
        q = deque()
        out = []
        if head is None:
            return
        q.appendleft(head)
        while len(q)>0:
            top = q.pop()
            left = top.left
            right = top.right
            if left!=None:
                q.appendleft(left)
            if right!=None:
                q.appendleft(right)
            #if left==None and right==None: # used for only leaves
            out.append(top.val)
        return " ".join(out)

    #height of a node
    def height(self,head):
        if head==None:
            return 0
        l_height = self.height(head.left)
        r_height = self.height(head.right)
        return max(l_height+1,r_height+1)

    # printing nodes at level k
    def print_at_level(self,head,level,arr):
        if head==None:
            return
        if level==1:
            arr.append(head.val)
        self.print_at_level(head.left,level-1,arr)
        self.print_at_level(head.right,level-1,arr)

    #find diameter of tree
    def diameter(self,head):
        if head==None:
            return 0
        return max(self.diameter(head.left),self.diameter(head.right),1+self.height(head.left)+self.height(head.right))

    def lca(self,key1,key2,s1,s2,head):
        if head==None:
            return None
        if head.val==key1 or head.val==key2:
            return head

        left = self.lca(key1,key2,s1,s2,head.left)
        right = self.lca(key1,key2,s1,s2,head.right)

        if left and right:
            return head

        if left is None:
            return right
        elif right is None:
            return left

b_tree = Btree()
n = int(raw_input())
str = raw_input().split()
#print str
i=0
size = 3*n
while(i<size):
    b_tree.add_node(str[i],str[i+1],str[i+2])
    i += 3


arr = []
b_tree.print_at_level(b_tree.head,1,arr)
print " ".join(arr)
arr = []
b_tree.print_at_level(b_tree.head,2,arr)
print " ".join(arr)
arr = []
b_tree.print_at_level(b_tree.head,3,arr)
print " ".join(arr)
arr = []
b_tree.print_at_level(b_tree.head,4,arr)
print " ".join(arr)
print b_tree.diameter(b_tree.head)
