def minMoves(arr1, arr2):
    arr1 = [str(i) for i in arr1]
    arr2 = [str(i) for i in arr2]
    res = []

    for i in range(len((arr1))):
        numMoves = 0
        j = 0
        while j < len(arr1[i]):

            number1 = int(arr1[i][j])
            number2 = int(arr2[i][j])

            while number1 < number2:
                number1 += 1
                numMoves += 1

            while number1 > number2:
                number1 -= 1
                numMoves += 1

            j += 1
        res.append(numMoves)

    return res


arr1 = [456, 154]
arr2 = [123, 473]

# print(minMoves(arr1, arr2))


def minMoves2(arr1, arr2):
    res = []

    for i in range(len(arr1)):
        ans = 0
        while arr1[i] > 0 and arr2[i] > 0:
            a = arr1[i] % 10
            b = arr2[i] % 10

            if a > b:
                ans += a - b
            else:
                ans += b - a

            arr1[i] //= 10
            arr2[i] //= 10
        res.append(ans)

    return res


# print(minMoves2(arr1, arr2))


def topKFrequent(words, k):
    wordCount = {}
    words.sort()
    for word in words:
        if not wordCount.get(word):
            wordCount[word] = 1
        else:
            wordCount[word] += 1

    wordOccurrence = [[] for _ in range(len(words))]

    for word, count in wordCount.items():
        wordOccurrence[count].append(word)

    res = []

    for i in reversed(wordOccurrence):

        for w in i:
            if len(res) == k:
                break

            res.append(w)
            print(res)

    return res


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

print(topKFrequent(words, k))
