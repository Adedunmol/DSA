

from ast import List


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


#print(factorial(3))

def reverse_string(arr: List):
    if len(arr) == 1:
        return arr
    else:
        item = arr.pop(0)
        reverse_string(arr)
        arr.append(item)
    return

arr = ['h', 'e', 'l', 'l', 'o']

reverse_string(arr)

print(arr)