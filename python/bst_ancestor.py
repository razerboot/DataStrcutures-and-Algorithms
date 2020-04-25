class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class BST():
    def __init__(self):
        self.head = None

    def insert(self, head, value):
        if value > head.val:
            if head.right == None:
                head.right = Node(value)
            else:
                self.insert(head.right, value)
        else:
            if head.left == None:
                head.left = Node(value)
            else:
                self.insert( head.left, value)

    def find_ancestor(self, head, value1, value2):
        if head.val == value1 or head.val == value2:
            return head
        if head.val > value1 and head.val < value2:
            return head
        elif head.val < value1 and head.val < value2:
            return self.find_ancestor( head.left, value1, value2)
        else:
            return self.find_ancestor( head.right, value1, value2)

    def find_max(self, ancestor, value):
        while (ancestor.val != value):
            if value > ancestor.val:
                ancestor = ancestor.right
                maxi = ancestor.val
            else:
                ancestor = ancestor.left
        return max(maxi, value)


n = input()
nodes = map(int, raw_input().split())
value1, value2 = map(int, raw_input().split())
if value1 > value2:
    value1, value2 = value2, value1
btree = BST()
head=btree.head
head = Node(nodes[0])
for node in nodes:
    if node == head.val:
        continue
    btree.insert(head, node)
ancestor = btree.find_ancestor(head, value1, value2)
#print ancestor.val
if ancestor.val == value2:
    print value2
else:
    print btree.find_max(ancestor, value2)

