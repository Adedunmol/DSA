import random
from types import new_class

#arr = []

#for i in range(1000):
#    arr.append(random.randint(0, i))

#print(arr)

def quicksort(arr):

    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


#print(quicksort(arr))


def partition(arr, low, high):
    indexOfSmaller = low - 1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] < pivot:

            indexOfSmaller += 1
            arr[indexOfSmaller], arr[j] = arr[j], arr[indexOfSmaller]
    
    indexOfSmaller += 1
    arr[indexOfSmaller], arr[high] = arr[high], arr[indexOfSmaller]

    return indexOfSmaller


def updatedQuickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        partitionIndex = partition(arr, low, high)

        updatedQuickSort(arr, low, partitionIndex - 1)
        updatedQuickSort(arr, partitionIndex + 1, high)

newArr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

updatedQuickSort(newArr, 0, len(newArr) - 1)

print(newArr)
