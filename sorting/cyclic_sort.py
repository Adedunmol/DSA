def cyclicSort(arr):
    i = 0

    while i < len(arr):
        correct = arr[i] - 1

        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1


arr = [3, 5, 2, 1, 2]
# cyclicSort(arr)
# print(arr)


def missingNumber(arr):
    i = 0

    while i < len(arr):
        if arr[i] < len(arr) and arr[i] != arr[arr[i]]:
            arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
        else:
            i += 1

    for index in range(len(arr)):
        if index != arr[index]:
            return index

    return len(arr)


def findDisappeared(arr):
    i = 0
    res = []

    while i < len(arr):
        correct = arr[i] - 1

        if arr[i] != arr[correct]:
            arr[correct], arr[i] = arr[i], arr[correct]

        else:
            i += 1

    for i in range(len(arr)):

        if arr[i] != i + 1:
            res.append(i + 1)

    return res


arr = [4, 3, 2, 7, 8, 2, 3, 1]
# print(findDisappeared(arr))


def findDuplicateNumber(arr):
    i = 0

    while i < len(arr):
        correct = arr[i] - 1

        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

    for j in range(len(arr)):

        if j + 1 != arr[j]:
            return arr[j]


arr = [1, 3, 4, 2, 2]
print(findDuplicateNumber(arr))
print(arr)
