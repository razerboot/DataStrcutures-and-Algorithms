from linkedList import Node

class OrderedList():

    def __init__(self,head=None,last=None):
        self.head = head
        self.last = last

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        if not self.head:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
        else:
            current = self.head
            previous = None
            found = False
            while current != None:
                if current.getData() > item:
                    found = True
                    temp = Node(item)
                    temp.setNext(current)
                    if not previous:
                        self.head = temp
                    else:
                        previous.setNext(temp)
                    break
                else:
                    previous = current
                    current = current.getNext()
            if not found:
                self.addAtEnd(item)
        if not self.last:
            self.last = self.head

    def addAtEnd(self,item):
        temp = Node(item)
        self.last.setNext(temp)
        self.last = temp

    def sizeOfList(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        position = 0
        while current != None:
            if current.getData() == item:
                found = True
                position = position+1
                break
            else:
                position = position+1
                current = current.getNext()
        if not found:
            return "not found"
        else:
            return position

    def delete(self,item):
        current = self.head
        previous = None
        found = False
        while current != None:
            currentData = current.getData()
            if currentData == item:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                found = True

                break
            else:
                previous = current
                current = current.getNext()
        return found

mylist1 = OrderedList()

mylist1.add(32) #2
mylist1.add(54) #4
mylist1.add(12) #1
mylist1.add(65) #5
mylist1.add(72) #6
mylist1.add(23) #2
mylist1.add(92)
print mylist1.search(92)