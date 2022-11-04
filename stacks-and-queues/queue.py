class Queue:
    def __init__(self, array=[]) -> None:
        self.array = []
        if array:
            self.array = array

    def getBuffer(self):
        return self.array[:]

    def isEmpty(self):
        return len(self.array) == 0

    def peek(self):
        return self.array[0]

    def enqueue(self, value):
        return self.array.append(value)

    def dequeue(self):
        return self.array.pop(0)

    def length(self):
        return len(self.array)

    def __repr__(self) -> str:
        return f"Queue: {self.array}"


queue1 = Queue()

queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)

# print(queue1)

# queue1.dequeue()
# print(queue1)

# queue1.dequeue()
# print(queue1)


def queueAccessNthTopNode(queue, n):
    bufferArray = queue.getBuffer()
    if n <= 0:
        return "Error"

    bufferQueue = Queue(bufferArray)

    n -= 1
    while n != 0:
        bufferQueue.dequeue()
        n -= 1

    return bufferQueue.dequeue()


# print(queueAccessNthTopNode(queue1, 2))


def queueSearch(queue, element):
    bufferArray = queue.getBuffer()

    bufferQueue = Queue(bufferArray)

    while not bufferQueue.isEmpty():
        if bufferQueue.dequeue() == element:
            return True

    return False


class QueueStack:
    def __init__(self) -> None:
        self.inbox = Queue()

    def push(self, value):
        self.inbox.enqueue(value)

    def pop(self):
        size = self.inbox.length() - 1
        counter = 0
        bufferQueue = Queue()

        counter += 1
        while counter <= size:
            bufferQueue.enqueue(self.inbox.dequeue())
            counter += 1

        popped = self.inbox.dequeue()
        self.inbox = bufferQueue

        return popped

    def __repr__(self) -> str:
        return f"{self.inbox}"


stack = QueueStack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
