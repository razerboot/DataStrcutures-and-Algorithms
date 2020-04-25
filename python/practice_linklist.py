class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self,new_next):
        self.next=new_next

class List:
    def __init__(self):
        self.head = None
        self.last = None
    def is_empty(self):
        return (self.head == None)

    def add(self,data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
        if not self.last:
            self.last = self.head

    def add_at_end(self,data):
        temp = Node(data)
        if self.last:
            self.last.set_next(temp)
        self.last = temp
        if not self.head:
            self.head = self.last

    def count_iter(self):
        count = 0
        temp = self.head
        while temp!=None:
            count += 1
            temp = temp.get_next()
        return count

    def count_recu(self,head):
        if not head:
            return 0
        return 1 + self.count_recu(head.get_next())

    def get_count_recur(self):
        return self.count_recu(self.head)

    def search(self,data, head):
        if not head:
            return "False"
        if head.get_data() == data:
            return "True"+" "+str(1)
        temp = self.search(data,head.get_next()).split()
        if temp[0]=="True":
            return temp[0]+" "+str(1+int(temp[1]))
        else:
            return "False"

    def search_recur(self,data):
        return self.search(data,self.head)

    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head.next
        #temp = self.head
        #checking for loop
        while(fast_p and fast_p.next):
            if slow_p == fast_p:
                #temp = slow_p
                #return slow_p.data
                break
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        # if loop exists
        if slow_p==fast_p:
            slow_p = self.head
            while slow_p!=fast_p.next:
                slow_p = slow_p.next
                fast_p = fast_p.next
            fast_p.next=None
        #return temp.data

    def print_list(self):
        temp = self.head
        str1 = ""
        while temp is not None:
            if temp == self.head:
                str1 += str(temp.data)
            else:
                str1 += " "+str(temp.data)
            temp = temp.next
        return str1

    def reverse_list(self):
        prev = None
        current = self.head
        cmg = self.head.next
        while cmg is not None:
            #cprev.next,current.next = current,prev
            current.next=prev
            prev = current
            current = cmg
            cmg = cmg.next
        current.next = prev
        self.head = current

    def reverse_recursive(self,head):
        if head 



mylist = List()
mylist.add(32)
mylist.add(54)
mylist.add(12)
mylist.add(33)
mylist.add(34)

#mylist.head.next.next.next.next.next = mylist.head.next
#mylist.detect_loop()
print mylist.print_list()
mylist.reverse_list()
print mylist.print_list()
#print mylist.search_recur(33)
#print mylist.is_empty()