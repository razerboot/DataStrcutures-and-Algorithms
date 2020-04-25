#List: 5->6->3 // represents
#number
#365

class Node():
    def __init__(self, key):
        self.val = key
        self.next = None

def newNode(head1, head2, carry, newHead):
    newval = head1.val + head2.val + carry
    carry = newval / 10
    newval = newval % 10
    node = Node(newval)
    return carry,node

# first ll - number 99543 3->4->5->9->9
# second ll - number 632 2->3->6

ll1=Node(3)
ll1.next=Node(4)
ll1.next.next=Node(5)
ll1.next.next.next=Node(9)
ll1.next.next.next.next=Node(9)

ll2=Node(2)
ll2.next=Node(3)
ll2.next.next=Node(6)

head1 = ll1
head2 = ll2
carry = 0
newHead = None
curr=None
while (head1 != None and head2 != None):
    carry,node = newNode(head1, head2, carry, newHead)
    #print head1.val,head2.val
    #print carry,node.val
    if newHead==None:
        newHead=node
        curr=node
    else:
        curr.next=node
        curr=curr.next
    head1 = head1.next
    head2 = head2.next
# if still there are values in head2 or head1
if head1 == None:
    while (head2 != None):
        carry,node = newNode(Node(0), head2, carry, newHead)
        curr.next=node
        curr=curr.next
        head2 = head2.next
else:
    while (head1 != None):
        #print head1.val
        carry,node = newNode(head1, Node(0), carry, newHead)
        #print carry,node.val
        curr.next = node
        curr = curr.next
        head1 = head1.next
if head1 == None and head2 == None and carry != 0:
    node = Node(1)
    curr.next = node

while(newHead!=None):
    print newHead.val,
    newHead=newHead.next