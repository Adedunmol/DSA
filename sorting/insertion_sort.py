def insertionSort(arr):

    for i in range(len(arr) - 1):

        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


arr = [0, -23, 56, 18]
insertionSort(arr)
print(arr)
