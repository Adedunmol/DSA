def bubbleSort(arr):
    swapped = None
    for i in range(len(arr)):
        swapped = False
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True

        if swapped == False:
            break


arr = [3, 1, 5, 2, 4]
bubbleSort(arr)
print(arr)
