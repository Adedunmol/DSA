from typing import List


class Stack:
    def __init__(self, array=[]) -> None:
        self.array = []
        if array:
            self.array = array

    def getBuffer(self) -> List:
        return self.array[:]

    def isEmpty(self):
        return len(self.array) == 0

    def peek(self):
        return self.array[len(self.array) - 1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def __repr__(self) -> str:
        return f"stack: {self.array}"


stack1 = Stack()

# stack1.push(10)
# print(stack1.peek())

# stack1.push(5)
# print(stack1.peek())

# stack1.push(1)
# stack1.push(2)
# stack1.push(3)

# stack1.pop()
# stack1.pop()
# stack1.pop()


def stackAccessNthTopNode(stack: Stack, n: int):
    bufferArray = stack.getBuffer()
    if n <= 0:
        return "error"

    bufferStack = Stack(bufferArray)

    n -= 1
    while n != 0:
        bufferStack.pop()
        n -= 1

    return bufferStack.pop()


stack2 = Stack()

stack2.push(1)
stack2.push(2)
stack2.push(3)

# print(stackAccessNthTopNode(stack2, 2))

# print(stack2)


def stackSearch(stack, element):
    bufferArray = stack.getBuffer()

    bufferStack = Stack(bufferArray)

    while not bufferStack.isEmpty():
        if bufferStack.pop() == element:
            return True

    return False


def isValid(s: str) -> bool:
    stack = []
    opening = "({["
    closing = {"(": ")", "{": "}", "[": "]"}

    for i in s:
        if i in opening:
            stack.append(i)
        else:
            if stack:
                lastPar = stack[-1]
                if closing[lastPar] == i:
                    stack.pop()
                else:
                    return False
            else:
                return False

    return len(stack) == 0


print(isValid("([}}])"))


class TwoStackQueue:
    def __init__(self) -> None:
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        self.inbox.push(value)

    def dequeue(self):
        if self.outbox.isEmpty():
            while not self.inbox.isEmpty():
                self.outbox.push(self.inbox.pop())

        return self.outbox.pop()

    def __repr__(self) -> str:
        return f"Queue: {self.inbox}"


queue = TwoStackQueue()

# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print(queue)

# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())


class MinStack:
    def __init__(self) -> None:
        self.mainStack = []
        self.sortedStack = []

    def push(self, val):
        self.mainStack.append(val)

        if len(self.sortedStack) != 0:
            tempStack = []

            while len(self.sortedStack) != 0 and val > self.sortedStack[-1]:
                tempStack.append(self.sortedStack.pop())

            self.sortedStack.append(val)

            while len(tempStack) != 0:
                self.sortedStack.append(tempStack.pop())
        else:
            self.sortedStack.append(val)

    def getMin(self):
        return self.sortedStack[-1]

    def top(self):
        return self.mainStack[-1]

    def pop(self):
        tempStack = []
        popped = self.mainStack.pop()

        while len(self.sortedStack) != 0:
            sortedPopped = self.sortedStack.pop()
            if sortedPopped == popped:
                break
            tempStack.append(sortedPopped)

        while len(tempStack) != 0:
            self.sortedStack.append(tempStack.pop())

    def __repr__(self) -> str:
        return f"Main: {self.mainStack}, Sorted: {self.sortedStack}"


minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print(minStack.getMin())

minStack.pop()
print(minStack.top())

print(minStack.getMin())
