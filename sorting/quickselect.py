from traceback import print_tb


def partition(arr, low, high):

    pivot = arr[high]
    j = low - 1

    for i in range(low, high):

        if arr[i] < pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]

    j += 1
    arr[j], arr[high] = arr[high], arr[j]

    return j


def quickSelect(arr, low, high, k):

    pIndex = partition(arr, low, high)

    if pIndex == (k - 1):
        return arr[pIndex]
    elif pIndex > (k - 1):
        return quickSelect(arr, low, pIndex - 1, k)
    else:
        return quickSelect(arr, pIndex + 1, high, k)


arr = [1, 3, 3, -2, 3, 14, 7, 8, 1, 2, 2]
# print(quickSelect(arr, 0, len(arr) - 1, 10))


def quickSelectMax(arr, low, high, k):
    correct = len(arr) - k
    pIndex = partition(arr, low, high)

    if pIndex == correct:
        return arr[pIndex]
    elif pIndex > correct:
        return quickSelectMax(arr, low, pIndex - 1, k)
    else:
        return quickSelectMax(arr, pIndex + 1, high, k)


arr = [3, 2, 1, 5, 6, 4]
arr2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# print(quickSelectMax(arr2, 0, len(arr2) - 1, 4))


class Solution:
    def findKthLargest(self, arr, k: int) -> int:

        return self.quickSelect(arr, 0, len(arr) - 1, k)

    def quickSelect(self, arr, low, high, k):

        correct = len(arr) - k
        pIndex = self.partition(arr, low, high)

        if pIndex == correct:
            return arr[pIndex]
        elif pIndex > correct:
            return self.quickSelect(arr, low, pIndex - 1, k)
        else:
            return self.quickSelect(arr, pIndex + 1, high, k)

    def partition(self, arr, low, high):

        pivot = arr[high]
        j = low - 1

        for i in range(low, high):

            if arr[i] < pivot:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]

        j += 1
        arr[j], arr[high] = arr[high], arr[j]

        return j


solution = Solution()
print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
