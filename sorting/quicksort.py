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


arr = [4, 3, 1, 5, 2, 3, 4, 5, 2]


def quicksort(arr, low, high):

    if low < high:
        pIndex = partition(arr, low, high)
        quicksort(arr, low, pIndex - 1)
        quicksort(arr, pIndex + 1, high)

    return


quicksort(arr, 0, len(arr) - 1)
print(arr)
