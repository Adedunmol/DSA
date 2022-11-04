def mergeSort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = mergeSort(list(arr[0:mid]))
    right = mergeSort(list(arr[mid : len(arr)]))

    return merge(left, right)


def merge(first, second):
    mix = []

    i = 0
    j = 0
    k = 0

    while i < len(first) and j < len(second):

        if first[i] < second[j]:
            mix.append(first[i])
            i += 1
        else:
            mix.append(second[j])
            j += 1

        k += 1

    while i < len(first):
        mix.append(first[i])
        i += 1
        k += 1

    while j < len(second):
        mix.append(second[j])
        j += 1
        k += 1

    return mix


arr = [5, 4, 3, 2, 1]
print(mergeSort(arr))
