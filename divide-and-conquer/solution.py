
from ast import Pass
from xml.dom.expatbuilder import parseString


arr = [2, 4, 6,]

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


def countItems(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + countItems(arr[1:])


def findMax(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        max = arr[0] if arr[0] > findMax(arr[1:]) else findMax(arr[1:])
        return max


my_list = [1, 3, 5, 7, 9]

def binary_search(arr, low, high, target):
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if len(arr) == 1:
        return None

    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)

    else:
        return binary_search(arr, mid + 1, high, target)

#print(countItems(arr))
#print(sum(arr))
#print(findMax(arr))

print(binary_search(my_list, low=0, high=len(my_list) - 1, target=9))