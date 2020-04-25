class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class llist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head==None

    def add_node(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def detect_loop(self):
        slow = self.head
        fast = self.head.next
        # detect loop
        while(fast and fast.next):
            if self==fast:
                break
            slow = slow.next
            fast =fast.next.next
        # move slow pointer from start and fast at meeting point with same speed till they meet which is the loop point
        #here we are checking slow!=fast.next bcoz both fast and slow will meet one step earlier instead of m since we intialized fast at one step ahead
        #of slow for not breaking the first loop at first step itself
        if slow==fast:
            slow = self.head
            while(slow!=fast.next):
                slow = slow.next
                fast = fast.next
            fast.next = None