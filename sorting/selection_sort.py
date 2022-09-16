def selection_sort(arr):

    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[min], arr[i] = arr[i], arr[min]


arr = [3, 1, 5, 2, 4]
selection_sort(arr)
print(arr)
