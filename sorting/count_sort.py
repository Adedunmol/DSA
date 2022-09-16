def countSort(array):
    hash = {}
    countArr = []

    for i in range(len(array)):
        if not hash.get(array[i]):
            hash[array[i]] = 1
        else:
            hash[array[i]] += 1

    for key, value in hash.items():

        for j in range(value):
            countArr.append(key)

    return countArr


print(countSort([6, 1, 23, 2, 3, 2, 1, 2, 2, 3, 3, 1, 123, 123, 4, 2, 3]))
