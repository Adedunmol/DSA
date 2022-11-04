import py_compile


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    head = None

    def insertFirst(self, val):
        node = Node(val)
        node.next = self.head
        node.prev = None

        if self.head != None:
            self.head.prev = node

        self.head = node

    def insertLast(self, val):
        node = Node(val)
        last = self.head
        node.next = None

        if self.head == None:
            node.prev = None
            self.head = node
            return

        while last.next != None:
            last = last.next

        node.prev = last
        last.next = node

    def find(self, value):
        node = self.head
        while node != None:
            if node.value == value:
                return node
            node = node.next

        return None

    def insertAfter(self, after, val):
        p = self.find(after)

        if p == None:
            print("does not exist")
            return

        node = Node(val)
        node.next = p.next
        p.next = node
        node.prev = p
        if node.next != None:
            node.next.prev = node

    def display(self):
        node = self.head
        last = None
        res = ""
        while node is not None:
            res += str(node.value) + " -> "
            last = node
            node = node.next

        res += "END"
        print(res)

        res = ""
        while last is not None:
            res += str(last.value) + " -> "
            last = last.prev

        res += "START"
        print("Print in reverse")
        print(res)


doublyLinkedList = DoublyLinkedList()
doublyLinkedList.insertFirst(3)
doublyLinkedList.insertFirst(2)
doublyLinkedList.insertFirst(8)
doublyLinkedList.insertFirst(17)

doublyLinkedList.insertLast(99)

doublyLinkedList.insertAfter(99, 65)

doublyLinkedList.display()
