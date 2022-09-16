

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    
    return newArr

arr = [5, 3, 6, 2, 10]


def newSelectionSort(arr):

    for i in range(len(arr)):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


print(newSelectionSort(arr))