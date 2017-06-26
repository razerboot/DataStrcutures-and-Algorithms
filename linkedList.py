class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        if not self.last:
            self.last = self.head

    def addAtEnd(self, item):
        temp = Node(item)
        self.last.setNext(temp)
        self.last = temp

    def sizeOfList(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        position = 0
        while current != None:
            if current.getData() == item:
                found = True
                position = position + 1
                break
            else:
                position = position + 1
                current = current.getNext()
        if not found:
            return "not found"
        else:
            return "position of the element: " + str(position)

    def delete(self, item):
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


mylist1 = UnorderedList()
mylist1.add(32)
mylist1.add(54)
mylist1.add(12)
mylist1.addAtEnd(65)
mylist1.addAtEnd(72)
mylist1.add(23)
print mylist1.search(72)
