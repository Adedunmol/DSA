from .heaps import Heap


class MinHeap(Heap):
    def __init__(self) -> None:
        super().__init__()
        self.items = []

    def bubbleDown(self):
        index = 0

        while self.leftChild(index) and self.leftChild(index) < self.items[index]:
            smallerIndex = self.leftChildIndex(index)
            if (
                self.rightChild(index)
                and self.rightChild(index) < self.items[smallerIndex]
            ):
                smallerIndex = self.rightChildIndex(index)

            self.swap(smallerIndex, index)
            index = smallerIndex

    def siftUp(self, i):
        parent = self.parentIndex(i)

        while i != 0 and self.items[i] < self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = self.parentIndex(i)

    def siftDown(self, i):
        left = self.leftChildIndex(i)
        right = self.rightChildIndex(i)

        while (left < len(self.items) and self.items[i] > self.items[left]) or (
            right < len(self.items) and self.items[i] > self.items[right]
        ):
            smallest = (
                left
                if (right >= len(self.items) or self.items[left] < self.items[right])
                else right
            )
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            i = smallest
            left = self.leftChildIndex(i)
            right = self.rightChildIndex(i)
