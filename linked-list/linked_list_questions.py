from email import header


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

    def insertRec(self, val, index):
        self.head = self.insertRecVal(val, index, self.head)

    def insertRecVal(self, val, index, node):
        if index == 0:
            temp = Node(val)
            temp.next = node
            self.size += 1
            return temp

        node.next = self.insertRecVal(val, index - 1, node.next)
        return node

    def duplicates(self):
        node = self.head

        while node.next != None:
            if node.value == node.next.value:
                node.next = node.next.next
                self.size -= 1
            else:
                node = node.next

        self.tail = node
        self.tail.next = None

    def merge(first, second):
        f = first.head
        s = second.head

        ans = LinkedList()

        while f != None and s != None:
            if f.value < s.value:
                ans.insertLast(f.value)
                f = f.next
            else:
                ans.insertLast(s.value)
                s = s.next

        while f != None:
            ans.insertLast(f.value)
            f = f.next

        while s != None:
            ans.insertLast(s.value)
            s = s.next

        return ans

    def hasCycle(self, head) -> bool:
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

    def lengthOfCycle(self, head) -> bool:
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                temp = slow
                length = 0

                temp = temp.next
                length += 1

                while temp != slow:
                    temp = temp.next
                    length += 1

                return length

        return 0

    def detectCycle(self, head):
        length = self.lengthOfCycle(head)

        if length == 0:
            return None

        f = head
        s = head

        while length > 0:
            s = s.next
            length -= 1

        while f != s:
            f = f.next
            s = s.next

        return s

    def detectCycle2(self, head):
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break

        slow2 = head
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next

        return slow

    def isHappy(self, n):
        slow = n
        fast = n

        slow = self.findSquare(slow)
        fast = self.findSquare(self.findSquare(fast))

        while slow != fast:
            slow = self.findSquare(slow)
            fast = self.findSquare(self.findSquare(fast))

        if slow == 1:
            return True

        return False

    def findSquare(self, n):
        ans = 0
        while n > 0:
            rem = n % 10
            ans += rem * rem
            n //= 10
        return ans

    def middleNode(self, head):
        slow = head
        fast = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head

        mid = self.middleNode(head)
        left = self.mergeSort(head)
        right = self.mergeSort(mid)

        return self.merge(left, right)

    def reverse(self, node):
        if node == self.tail:
            self.head = self.tail
            return

        self.reverse(node.next)
        self.tail.next = node
        self.tail = node
        self.tail.next = None

    def reverseLoop(self, node):
        if self.size < 2:
            return

        prev = None
        present = self.head
        next = present.next

        while present != None:
            present.next = prev
            prev = present
            present = next
            if next != None:
                next = next.next

        self.head = prev

    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        current = head
        prev = None
        i = 0
        while i < left - 1 and current != None:
            prev = current
            current = current.next
            i += 1

        last = prev
        newEnd = current
        next = current.next
        i = 0
        while i < right - left + 1 and current != None:
            current.next = prev
            prev = current
            current = next
            if next != None:
                next = next.next
            i += 1

        if last != None:
            last.next = prev
        else:
            head = prev

        newEnd.next = current
        return head

    def isPalindrome(self, head):
        mid = self.middleNode(head)
        headSecond = self.reverseLoop(mid)
        rereverseHead = headSecond

        # compare both halves
        while head != None and headSecond != None:
            if head.val != headSecond.val:
                break
            head = head.next
            headSecond = headSecond.next

        self.reverseLoop(rereverseHead)

        return head == None or headSecond == None

    def reorderList(self, head):
        if head == None or head.next == None:
            return

        mid = self.middleNode(head)
        hs = self.reverseLoop(mid)
        hf = head

        # rearrange
        while hf != None and hs != None:
            temp = hf.next
            hf.next = hs
            hf = temp

            temp = hs.next
            hs.next = hf
            hs = temp

        if hf != None:
            hf.next = None


first = LinkedList()
second = LinkedList()

first.insertLast(1)
first.insertLast(3)
first.insertLast(5)

second.insertLast(1)
second.insertLast(2)
second.insertLast(9)
second.insertLast(14)

ans = LinkedList.merge(first, second)
ans.display()
