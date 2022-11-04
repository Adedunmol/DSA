class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        newListNode = ListNode()
        dummyHead = newListNode
        rem = 0

        while l1 != None and l2 != None:

            newVal = l1.val + l2.val + rem

            if not self.isDouble(newVal):
                rem = 0
                newNode = ListNode(newVal)
                newListNode.next = newNode
                newListNode = newNode
            else:
                tens, unit = self.single(newVal)
                rem = tens
                newNode = ListNode(unit)
                newListNode.next = newNode
                newListNode = newNode

            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            newVal = l1.val + rem

            if not self.isDouble(newVal):
                newNode = ListNode(newVal)
                newListNode.next = newNode
                newListNode = newNode
            else:
                tens, unit = self.single(newVal)
                rem = tens
                newNode = ListNode(unit)
                newListNode.next = newNode
                newListNode = newNode
            l1 = l1.next

        while l2 != None:
            newVal = l2.val + rem

            if not self.isDouble(newVal):
                newNode = ListNode(newVal)
                newListNode.next = newNode
                newListNode = newNode
            else:
                tens, unit = self.single(newVal)
                rem = tens
                newNode = ListNode(unit)
                newListNode.next = newNode
                newListNode = newNode
            l2 = l2.next

        print("rem", rem)
        if rem != 0:
            # tens, unit = self.single(newVal)
            newNode = ListNode(rem)
            newListNode.next = newNode
            newListNode = newNode

        return dummyHead.next

    def single(self, n):
        unit = n % 10
        n //= 10
        tens = n % 10

        return tens, unit

    def isDouble(self, n):
        n = n // 10

        return n != 0

    def swapPairs(self, head):
        if head == None or head.next == None:
            return head

        prev = head
        current = head

        while current != None:

            current = current.next

            prev.next = current.next
            current.next = prev

            current = prev.next
            prev = prev.next

            print(prev.val)
            print(current.val)

        return head

    def mergeTwoLists(self, list1, list2):

        newListNode = ListNode()
        dummyHead = newListNode

        while list1 != None and list2 != None:

            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                newListNode.next = newNode
                newListNode = newNode
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                newListNode.next = newNode
                newListNode = newNode
                list2 = list2.next

        while list1 != None:
            newNode = ListNode(list1.val)
            newListNode.next = newNode
            newListNode = newNode
            list1 = list1.next

        while list2 != None:
            newNode = ListNode(list2.val)
            newListNode.next = newNode
            newListNode = newNode
            list2 = list2.next

        return dummyHead.next


firstList1 = ListNode(1)
firstList2 = ListNode(2)
firstList3 = ListNode(3)
firstList4 = ListNode(4)
# firstList5 = ListNode(9)
# firstList6 = ListNode(9)
# firstList7 = ListNode(9)

firstList1.next = firstList2
firstList2.next = firstList3
firstList3.next = firstList4


# firstList4.next = firstList5
# firstList5.next = firstList6
# firstList6.next = firstList7

secondList1 = ListNode(9)
secondList2 = ListNode(9)
secondList3 = ListNode(9)
secondList4 = ListNode(9)

secondList1.next = secondList2
secondList2.next = secondList3
secondList3.next = secondList4

solution = Solution()

head = solution.mergeTwoLists(firstList1, firstList1)

while head is not None:
    print(head.val)
    head = head.next
