class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
            self.tail = node

        self.tail.next = node
        node.next = self.head
        self.tail = node

    def display(self):
        node = self.head
        res = ""
        if self.head != None:
            res += str(node.val) + " -> "
            node = node.next
            while node != self.head:
                res += str(node.val) + " -> "
                node = node.next

        res += "HEAD"
        print(res)

    def delete(self, val):
        node: Node = self.head

        if node == None:
            return

        if node.val == val:
            self.head = self.head.next
            self.tail.next = self.head

        n = node.next
        if n.val == val:
            node.next = n.next
        node = node.next

        while node != self.head:
            n = node.next
            if n.val == val:
                node.next = n.next
                break
            node = node.next


circularLinkedList = CircularLinkedList()

circularLinkedList.insert(23)
circularLinkedList.insert(3)
circularLinkedList.insert(19)
circularLinkedList.insert(75)

circularLinkedList.delete(19)

circularLinkedList.display()
