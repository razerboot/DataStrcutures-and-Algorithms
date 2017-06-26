class Node():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

class BST():
    def __init__(self):
        self.head=None

    def insert(self,head,key):
        if key>head.val:
            if head.right==None:
                head.right=Node(key)
            else:
                self.insert(head.right,key)
        elif key<head.val:
            if head.left==None:
                head.left=Node(key)
            else:
                self.insert(head.left, key)
        return

    def inorder_succ(self,node):
        succ = None
        if node.right==None:
            succ = self.inorder_succ_null(self.head,node,succ)
        else:
            succ = self.find_min(node.right)
        return succ

    def inorder_succ_null(self,head,node,succ):
        if head==None:
            return None
        while(head!=None):
            if node.val>head.val:
                head = head.right
            elif node.val<head.val:
                succ = head
                head=head.left
            else:
                break
        return succ

    def find_min(self,head):

        if head is None:
            return

        while(head.left!=None):
            head = head.left
        return head

    def lca(self,key1,key2,head):
        if head==None:
            return None
        if key1<head.val and key2<head.val:
            return self.lca(key1,key2,head.left)
        elif key1>head.val and key2>head.val:
            return self.lca(key1,key2,head.right)
        else:
            return head

    def traverse_inorder(self,head,arr):
        if head==None:
            return
        self.traverse_inorder(head.left,arr)
        arr.append(head.val)
        self.traverse_inorder(head.right,arr)
        return

    # checking whether a bt is a bst or not #application of dfs inorder
    def check_bst(self,head,prev):
        if head==None:
            return True
        if not self.check_bst(head.left,prev):
            return False
        if head.val<prev[0]:
            return False
        prev[0] = head.val
        if not self.check_bst(head.right,prev):
            return False
        return True

    #returning kth element using in order traversal
    def return_k(self,head,k,c):
        if head==None:
            return None
        left = self.return_k(head.left,k,c)

        if left:
            return left
        c[0]+=1
        if k==c[0]:
            return head.val
        right=self.return_k(head.right,k,c)

        if right:
            return right

    #swap wrongly inserted elements
    def swap(self,head,arr,prev):
        if head==None:
            return
        if len(arr)>2:
            return
        self.swap(head.left,arr,prev)
        if prev[0].val>head.val:
            if arr==[]:
                arr.append(prev[0])
                arr.append(head)
            else:
                arr.append(head)
        prev[0] = head
        self.swap(head.right,arr,prev)

        return

    def delete(self,head,key):
        if key>head.val:
            head.right=self.delete(head.right, key)
        elif key<head.val:
            head.left = self.delete(head.left, key)
        else:
            if head.left==None:
                temp = head.right
                head=None
                return temp
            elif head.right==None:
                temp=head.left
                head=None
                return temp
            temp = self.inorder_succ(head)
            head.val = temp.val
            head.right = self.delete(head.right,temp.val)

        return head


b_tree = BST()
b_tree.head=Node(14)
b_tree.insert(b_tree.head,8)
b_tree.insert(b_tree.head,21)
b_tree.insert(b_tree.head,4)
b_tree.insert(b_tree.head,11)
b_tree.insert(b_tree.head,17)
b_tree.insert(b_tree.head,25)
b_tree.insert(b_tree.head,2)
b_tree.insert(b_tree.head,6)
b_tree.insert(b_tree.head,9)
b_tree.insert(b_tree.head,13)
b_tree.insert(b_tree.head,15)
b_tree.insert(b_tree.head,19)
b_tree.insert(b_tree.head,23)
b_tree.insert(b_tree.head,1)
b_tree.insert(b_tree.head,3)
b_tree.insert(b_tree.head,5)
b_tree.insert(b_tree.head,7)
b_tree.insert(b_tree.head,10)
b_tree.insert(b_tree.head,12)
b_tree.insert(b_tree.head,16)
b_tree.insert(b_tree.head,18)
b_tree.insert(b_tree.head,20)
b_tree.insert(b_tree.head,22)
b_tree.insert(b_tree.head,24)
b_tree.insert(b_tree.head,26)

b_tree.head.left.val,b_tree.head.left.left.right.right.val = b_tree.head.left.left.right.right.val,b_tree.head.left.val
arr=[]
b_tree.traverse_inorder(b_tree.head,arr)
print arr
#print b_tree.find_min(b_tree.head).val
#b_tree.delete(b_tree.head,1)
print b_tree.check_bst(b_tree.head,[-422234245])
#print b_tree.lca(10,8,b_tree.head).val
#print b_tree.return_k(b_tree.head,21,[0])
#temp = Node(-24346321)
#arr = []
#b_tree.swap(b_tree.head,arr,[temp])

#if len(arr)==2:
#    arr[0].val,arr[1].val = arr[1].val,arr[0].val
#elif len(arr)==3:
#    arr[0].val, arr[2].val = arr[2].val, arr[0].val

#arr=[]
#b_tree.traverse_inorder(b_tree.head,arr)
#print arr

#print arr[0].val
#print arr[1].val
#print arr[2].val
