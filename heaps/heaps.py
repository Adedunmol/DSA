import heapq


class Heap:
    def __init__(self) -> None:
        self.items = []

    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def parentIndex(self, index):
        return (index - 1) // 2

    def leftChildIndex(self, index):
        return (index * 2) + 1

    def rightChildIndex(self, index):
        return (index * 2) + 2

    def parent(self, index):
        return self.items[self.parentIndex(index)]

    def leftChild(self, index):
        return self.items[self.leftChildIndex(index)]

    def rightChild(self, index):
        return self.items[self.rightChildIndex(index)]

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def fillCups(amount) -> int:
    heap = amount
    heapq.heapify(heap)
    ans = 0

    while heap:

        while heap and heap[0] == 0:
            heapq.heappop(heap)

        if len(heap) == 1:
            prev = heapq.heappop(heap)
            cup = 0 if prev - 2 < 0 else prev - 2
            heapq.heappush(heap, cup)
        elif len(heap) > 1:
            cup1 = heapq.heappop(heap) - 1
            cup2 = heapq.heappop(heap) - 1

            heapq.heappush(heap, cup1)
            heapq.heappush(heap, cup2)

        if heap:
            ans += 1

    return ans


print(fillCups([1, 4, 2]))
