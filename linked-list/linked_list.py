class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    head = None
    tail = None

    def __init__(self) -> None:
        self.size = 0

    def insertFirst(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

        if self.tail == None:
            self.tail = self.head

        self.size += 1

    def insertLast(self, val):
        if self.tail == None:
            self.insertFirst(val)
            return

        node = Node(val)
        self.tail.next = node
        self.tail = node

        self.size += 1

    def insert(self, val, index):
        if index == 0:
            self.insertFirst(val)
            return

        if index == self.size:
            self.insertLast(val)
            return

        temp = self.head
        for i in range(1, index):
            temp = temp.next

        node = Node(val)
        node.next = temp.next
        temp.next = node

        self.size += 1

    def display(self):
        temp = self.head
        res = ""
        while temp != None:
            res += str(temp.value) + " -> "
            temp = temp.next
        res += "END"
        print(res)

    def deleteFirst(self):
        val: int = self.head.value
        self.head: Node = self.head.next

        if self.head == None:
            self.tail = None

        self.size -= 1
        return val

    def deleteLast(self):
        if self.size <= 1:
            return self.deleteFirst()

        secondLast = self.get(self.size - 2)
        val = self.tail.value
        self.tail = secondLast
        self.tail.next = None
        self.size -= 1

        return val

    def get(self, index):
        node = self.head
        for i in range(index):
            node = node.next

        return node


linkedList = LinkedList()

linkedList.insertFirst(3)
linkedList.insertFirst(2)
linkedList.insertFirst(8)
linkedList.insertFirst(17)

linkedList.insertLast(99)

linkedList.insert(100, 3)

print(linkedList.deleteFirst())

linkedList.display()

print(linkedList.deleteLast())

linkedList.display()
