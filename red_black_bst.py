class Node():
    def __init__(self,key):
        self.left=None
        self.right=None
        self.color = "Black"
        self.val=None
        self.parent=None
        if key is not None:
            self.new_node(key)

    def new_node(self,key):
        self.left=Node(None)
        self.right=Node(None)
        self.val=key
        self.color="Red"

class RBT():
    def __init__(self):
        self.root=None

    #find parent
    def grandparent(self,node):
        gp = None
        if node.parent and node.parent.parent:
            gp=node.parent.parent
        return gp
    #find uncle
    def find_uncle(self,node):
        gp = self.grandparent(node)
        if gp==None:
            return None,None
        elif node.parent==gp.left:
            return gp.right,gp
        elif node.parent==gp.right:
            return gp.left,gp

    def rotate_left(self,n,p,gp):
        l = n.left
        if gp:
            if gp.left==p:
                gp.left=n
            elif gp.right==p:
                gp.right=n
            n.parent=gp
        else:
            self.root=n
            n.parent=None
        n.left=p
        p.right=l
        p.parent=n
        l.parent=p

    def rotate_right(self,n,p,gp):
        r = n.right
        if gp:
            if gp.left==p:
                gp.left=n
            elif gp.right==p:
                gp.right=n
            n.parent=gp
        else:
            self.root=n
            n.parent=None
        n.right=p
        p.left=r
        p.parent = n
        r.parent = p

    def insert(self,n):
        c = self.root
        if c==None:
            self.root=n
        else:
            p = c
            while(c.val):
                p=c
                if n.val>c.val:
                    c=c.right
                else:
                    c=c.left
            n.parent=p
            if p.val>n.val:
                p.left=n
            else:
                p.right=n
        self.insert_1(n)


    #case 1 where root is red or node has no parent implies root is node
    def insert_1(self,n):
        if n.parent==None :
            n.color="Black"
        else:
            self.insert_2(n)

    #case2 where node is not root and parent is black
    def insert_2(self,n):
        if n.parent.color=="Black":
            #print "cool"
            return
        self.insert_3(n)

    #case 3 where parent is red and uncle is red
    def insert_3(self,n):
        u,gp = self.find_uncle(n)
        if u!=None and u.color=="Red":
            n.parent.color = "Black"
            u.color = "Black"
            gp.color="Red"
            self.insert_1(gp)
        else:
            self.insert_4(n,gp)

    #case 4 where color of uncle is black and node is right to parent and parent is left to gp
    def insert_4(self,n,gp):
        p = n.parent
        if gp.left and p.right==n and gp.left==p:
            self.rotate_left(n,n.parent,gp)
            p=n
        elif gp.right and p.left==n and gp.right==p:
            self.rotate_right(n,p,gp)
            p=n
        self.insert_5(p,gp)
    # case 5 where color of uncle is black but node is left to parent and parent is left gp
    def insert_5(self,p,gp):
        p.color = "Black"
        gp.color = "Red"
        if gp.left==p:
            self.rotate_right(p,gp,gp.parent)
        elif gp.right==p:
            self.rotate_left(p,gp,gp.parent)

    def find_height(self,n):
        if n.val==None:
            return 0
        l = self.find_height(n.left)
        r = self.find_height(n.right)
        return max(l+1,r+1)

    def in_order(self,head):
        if head.val==None:
            return
        self.in_order(head.left)
        print head.val
        self.in_order(head.right)
        return




rb_tree = RBT()
rb_tree.insert(Node(10))
rb_tree.insert(Node(12))
rb_tree.insert(Node(13))
rb_tree.insert(Node(15))
rb_tree.insert(Node(17))

#print rb_tree.root.val
#print rb_tree.root.color
print rb_tree.root.left.val
print rb_tree.root.right.left.val
#print rb_tree.root.left.color
#print rb_tree.root.right.color
print rb_tree.find_height(rb_tree.root)
print rb_tree.in_order(rb_tree.root)

